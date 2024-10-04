# General
These are just notes for myself if I ever want to host the application (again).

# Backend (Vercel)
- Navigate to `backend`
- Download vercel cli with: `npm i -g vercel`
- Login: `vercel login`
- Load the project: `vercel .`
- When asked to link to existing project, say yes and type the name of the project (currently `pokedoku2-backend`)
- To deploy to prod manually: `vercel --prod`

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
