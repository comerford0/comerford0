# Easy source control and web display of your professional life

## from 0 to hero in 5 easy steps 

[Github Quickstart Guide](https://docs.github.com/en/pages/quickstart)

### Fork this repository into your own github profile

**Important** Name this repository {your github username}.github.io
Also, it needs to be public...

### Clone that repository locally and update.

Most important 2 things to update is portfolio.yaml & img/main_image.jpg

### UV Sync & Run main.py

This takes your YAML and uses the templates to make a index.html.
Then Push this back up to github

### Enable github pages

1. In the repository settings (on github) go to the pages tab
1. Click Deploy from a branch
1. Choose main (who uses anything else?)

### Go bask in your glory

Head on over to {your github username}.github.io (website)


### Optional final step for your own domain 

[Github guide on setting your own domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)

1. In the github repostiory settings, under pages enter your custom domain (this will add a CNAME file to your repository)
1. Head on over to your domain provider
1. for your chosen domain click manage DNS
1. Create A Records pointing to your domain name to the following IP addresses 
    ```
    185.199.108.153
    185.199.109.153
    185.199.110.153
    185.199.111.153
    ```
1. Create AAA Records pointing to your domain name to the following IP addresses 
    ```
    2606:50c0:8000::153
    2606:50c0:8001::153
    2606:50c0:8002::153
    2606:50c0:8003::153
    ```
