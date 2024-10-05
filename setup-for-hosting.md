# General
These are just notes for myself if I ever want to host the application (again).

# Backend (Vercel)
- Navigate to `backend`
- Download vercel cli with: `npm i -g vercel`
- Login: `vercel login`
- Load the project: `vercel .`
- When asked to link to existing project, say yes and type the name of the project (currently `pokedoku2-backend`)
- To deploy to prod manually: `vercel --prod`

### Database Setup
The backend also requires the postgres database to be set up. To do so:
- Copy your connection string and set it as `CONNECTION_STRING` in `.env`
- Run `python db.py`, which will connect to the db and create the tables required
- Optionally, run `python db_business.py` as well to create a puzzle to start off

# Frontend (GitHub pages)
- Navigate to `frontend`
- To deploy to prod manually:
```
npm run build
npm run deploy
```
Now, you can go to `https://<github-username>.github.io/pokedoku2/` and see your website.

# Workflows
Each time a new tag is pushed to main, workflows are triggered
that deploy both the frontend and backend.
