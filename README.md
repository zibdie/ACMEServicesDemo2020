# Panasonic Braven Spring 2020 Challenge - ACME Panel Concept

The code for a mockup panel demonstrated in front of Panasonic North America executives during the Panasonic Braven Spring 2020 Challenge. The panel design, along with our other suggestions, won us first place in the competition.

The panel was supposed to be a mockup and easily ran on a USB, hence why you see no real security or infastructure put in place.

The `requirements.txt` is just to install a package for the Python files that I made as helper files for me, not needed to run the website.

---

If you wish to test it out locally, you can spin up a Docker container by running these two commands

```
> docker build -t acmeservicesdemo2020 .
> docker run -d -p 8345:80 acmeservicesdemo2020
```