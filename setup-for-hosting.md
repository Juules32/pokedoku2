# General
These are just notes for myself if I ever want to host the application.
NOTE: The frontend is free to host on github, however, the backend will cost some amount of money to host on heroku.

# Backend
- Download Heroku CLI
- Navigate to `backend`
- Run the following commands:
```
heroku login
heroku create pokedoku2-backend
git init
git add .
git commit -m "Deploy To Heroku"
git remote add heroku https://git.heroku.com/pokedoku2-backend.git
git push heroku main
```

# Frontend
- Copy `.env` and rename it to `.env.production`
- Under `VITE_BACKEND_URL`, fill in `https://pokedoku2-backend-<uid>.herokuapp.com/`
> **_NOTE:_** Remember that heroku will generate a custom uid for the domain name.
- Run the following commands:
```
npm run build
npm run deploy
```

Now, you can go to `https://<github-username>.github.io/pokedoku2/` and see your website.