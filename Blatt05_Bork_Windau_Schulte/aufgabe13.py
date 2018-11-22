import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def aufgabe13():
    np.random.seed(8)
    data = DataFrame()
    #a)-----------------
    u = np.random.uniform(0,1,10**5)

    def energy_neutrino(u):
        return (1-u)**(-1/1.7)

    neutrino = np.array(energy_neutrino(u))
    E = neutrino

    data['Energy'] = Series(E)

    #b)-----------------------
    def probability(E):
        return (1-np.exp(-E/2))**3

    v = np.random.uniform(0,1,10**5)
    accepted_values_mask = (v <= probability(neutrino))

    plt.hist(neutrino, bins=np.logspace(0,2,100), density=True, histtype='bar', alpha=0.6, label='Signale')
    plt.hist(neutrino[accepted_values_mask], bins=np.logspace(0,2,100), density=True, histtype='bar', alpha=0.5, label='Signale mit Akzeptanz')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('E')
    plt.legend()
    plt.savefig('plothist.pdf')
    plt.clf()

    data['AcceptanceMask'] = Series(accepted_values_mask)

    #c)---------------------------------

    def polar_hits(N):
        u1 = np.random.uniform(0,1,N)
        u2 = np.random.uniform(0,1,N)
        v1 = 2*u1 - 1
        v2 = 2*u2 - 1
        s = v1**2 + v2**2
        A = s < 1
        s_accepted = s[A==1]
        if len(s_accepted) == len(s):
            x1 = v1*np.sqrt(-2/s_accepted * np.log(s_accepted))
            x2 = v2*np.sqrt(-2/s_accepted * np.log(s_accepted))
            return x1, x2, s_accepted
        else:
            l = len(s) - len(s_accepted)
            x1_2, x2_2, s_accepted_2 = polar_hits(l)
            s_accepted = np.append(s_accepted,s_accepted_2)
            x1 = v1*np.sqrt(-2/s_accepted * np.log(s_accepted))
            x2 = v2*np.sqrt(-2/s_accepted * np.log(s_accepted))
            x1 = np.append(x1,x1_2)
            x2 = np.append(x2,x2_2)
            x1 = x1[0:len(s_accepted)]
            x2 = x2[0:len(s_accepted)]
            return x1, x2, s_accepted

    def normal_hits(mu,sigma,rho,E):
        N =len(E)
        x1, x2, s = polar_hits(N)
        mu = mu[0:N]
        sigma = sigma[0:N]
        x_normal = np.sqrt(1-rho**2)*sigma*x1 + rho*sigma*x2 + mu
        x_normal = np.round(x_normal,0)
        x_normal_accepted = x_normal[x_normal > 0]
        if len(x_normal_accepted) == len(x_normal):
            return x_normal_accepted
        else:
            l = len(x_normal) - len(x_normal_accepted)
            x_normal_2 = normal_hits(mu,sigma,rho,E[0:l])
            x_normal_accepted = np.append(x_normal_accepted,x_normal_2)
            return x_normal_accepted

    mu = 10 * E
    sigma = 2 * E
    rho = 0

    N = normal_hits(mu,sigma,rho,E)

    data['NumberOfHits'] = Series(N)

    #d)------------------------------------------

    #pkt ziehen aus zwei gauß verteilungen mit mu 3 bzw 7 und sigma 1/log_10(N+1)
    def normal2D_hits_x(N):
        N_laenge = len(N)
        x1, x2, s = polar_hits(N_laenge)
        mu = 7
        sigma = 1/(np.log10(N+1))
        x = np.array(sigma*x1 + sigma*x2 + mu)
        mask = np.logical_or(x < 0, x > 10)
        while not np.sum(mask) == 0:
            x1_2, x2_2, s_2 = polar_hits(np.sum(mask))
            sigma = sigma[0:np.sum(mask)]
            x[mask] = sigma*x1_2 + sigma*x2_2 + mu
            mask = np.logical_or(x < 0, x > 10)
        return x

    def normal2D_hits_y(N):
        N_laenge = len(N)
        y1, y2, s = polar_hits(N_laenge)
        mu = 3
        sigma = 1/(np.log10(N+1))
        y = np.array(sigma*y1 + sigma*y2 + mu)
        mask = np.logical_or(y < 0, y > 10)
        while not np.sum(mask) == 0:
            y1_2, y2_2, s_2 = polar_hits(np.sum(mask))
            sigma = sigma[0:np.sum(mask)]
            y[mask] = sigma*y1_2 + sigma*y2_2 + mu
            mask = np.logical_or(y < 0, y > 10)
        return y

    x_hits = normal2D_hits_x(N)

    data['x'] = Series(x_hits)

    y_hits = normal2D_hits_y(N)

    data['y'] = Series(y_hits)

    data.to_hdf('NeutrinoMC.hdf5', key='Signal')

    plt.hist2d(x_hits,y_hits, bins = [50,50], range = [[-1,11],[-1,11]])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('detektor.pdf')
    plt.clf()

    #e)-------------------------------------
    noise = DataFrame()

    rho_noise = 0.5
    mu_noise = 2
    sig_noise = 1
    E_noise = np.zeros(10**7)

    def normal_hits_noise(mu,sigma,rho,E):
        N =len(E)
        x1, x2, s = polar_hits(N)
        x_normal = np.sqrt(1-rho**2)*sigma*x1 + rho*sigma*x2 + mu
        x_normal = np.round(x_normal,0)
        x_normal_accepted = x_normal[x_normal > 0]
        if len(x_normal_accepted) == len(x_normal):
            return x_normal_accepted
        else:
            l = len(x_normal) - len(x_normal_accepted)
            x_normal_2 = normal_hits_noise(mu,sigma,rho,E[0:l])
            x_normal_accepted = np.append(x_normal_accepted,x_normal_2)
            return x_normal_accepted


    log10_N_noise = normal_hits_noise(mu_noise,sig_noise,rho_noise,E_noise)
    N_noise = 10**log10_N_noise
    N_noise = np.round(N_noise,0)

    noise['NumberOfHits'] = Series(N_noise)

    #############################################################

    def normal2D_hits_x_noise(N):
        N_laenge = len(N)
        x1, x2, s = polar_hits(N_laenge)
        mu = 5
        sigma = 3
        rho = 0.5
        x = np.array(np.sqrt(1-rho**2)*sigma*x1 + rho*sigma*x2 + mu)
        mask = np.logical_or(x < 0, x > 10)
        while not np.sum(mask) == 0:
            x1_2, x2_2, s_2 = polar_hits(np.sum(mask))
            x[mask] = sigma*x1_2 + sigma*x2_2 + mu
            mask = np.logical_or(x < 0, x > 10)
        return x

    def normal2D_hits_y_noise(N):
        N_laenge = len(N)
        y1, y2, s = polar_hits(N_laenge)
        mu = 5
        sigma = 3
        rho = 0.5
        y = np.array(np.sqrt(1-rho**2)*sigma*y1 + sigma*y2 + mu)
        mask = np.logical_or(y < 0, y > 10)
        while not np.sum(mask) == 0:
            y1_2, y2_2, s_2 = polar_hits(np.sum(mask))
            y[mask] = sigma*y1_2 + sigma*y2_2 + mu
            mask = np.logical_or(y < 0, y > 10)
        return y

    x_noise = normal2D_hits_x_noise(E_noise)
    y_noise = normal2D_hits_y_noise(E_noise)

    plt.hist2d(x_noise,y_noise, bins = [50,50], range = [[-1,11],[-1,11]])
    plt.xlabel('x-Untergrund')
    plt.ylabel('y-Untergrund')
    plt.savefig('detektoruntergrund.pdf')
    plt.clf()

    plt.hist(log10_N_noise, bins=np.logspace(0,2,50), histtype='step')
    plt.xlabel('log(N-Untergrund)')
    plt.savefig('histuntergrund.pdf')
    plt.clf()

    noise['x'] = Series(x_noise)
    noise['y'] = Series(y_noise)

    noise.to_hdf('NeutrinoMC.hdf5', key='Background')

if __name__ == '__main__':
    aufgabe13()
