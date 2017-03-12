from credentials import DO_TOKEN, BASE_DOMAIN, DEPLOY
import digitalocean
manager = digitalocean.Manager(token=DO_TOKEN)

def get_domain():
    print(manager.get_domain(domain_name=BASE_DOMAIN).zone_file)


if __name__ == '__main__':
    get_domain()