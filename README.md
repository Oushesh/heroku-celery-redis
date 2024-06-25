## AIM:
   * Keep constantly polling the agent giving the json output
     of the pages in question.

     http://qgg8gwo.155.248.247.164.sslip.io/docs#/

## Deployment
    * Deployed on heroku at: https://heroku-backend-dom-f6f9a6e0eae5.herokuapp.com/docs#/default/home__post

    * For long running tasks:
      * Add Heroku Redis Add-on:
        *  heroku addons:create heroku-redis


## Celery and Redis:
   * Redis installation: pip3 install redis kombu
   * test redis: bash redis.sh

   * Entry point: main_celer.py  


   * Setup of redis on heroku: https://devcenter.heroku.com/articles/heroku-redis

   
## Ref: 
   * 