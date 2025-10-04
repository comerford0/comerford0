# Easy source control and web display of your professional life

## from 0 to hero in 5 easy steps 

[Github Quickstart Guide](https://docs.github.com/en/pages/quickstart)

### Fork this repository into your own github profile

**Important** Name this repository {your github username}.github.io
Also, it needs to be public...

### Clone that repository locally and update.

Most important 3 things to update is.
1. portfolio.yaml 
1. img/main_image.jpg

### UV Sync & Run main.py

This takes your YAML and uses the templates to make a index.html.
Then Push this back up to github

### Enable github pages

1. In the repository settings (on github) go to the pages tab
1. Click Deploy from a branch
1. Choose main (who uses anything else?)

### Go bask in your glory

Head on over to {your github username}.github.io (website)


### Optional final steps for your own domain 

[Github guide](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)

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
1. Create AAAA Records pointing to your domain name to the following IP addresses 
    ```
    2606:50c0:8000::153
    2606:50c0:8001::153
    2606:50c0:8002::153
    2606:50c0:8003::153
    ```
1. Finally make a C Name Record that points www to {your github username}.github.io

### Optional Verify your domain to enforce HTTPS

[Github Guide](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages)

1. On your github settings (top right of any page)
1. Click Pages on the left hand side
1. Click add a domain and enter your domain
1. follow instructions on addind a TXT record in your domain provider
1. Wait for verification
1. Enable force HTTPS on your repository page settings