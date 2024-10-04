# General
These are just notes for myself if I ever want to host the application (again).

# Backend (Vercel)
In the `root` folder:
- Download vercel cli with: `npm i -g vercel`
- Login: `vercel login`
- Load the project: `vercel .`
- When asked to link to existing project, say yes and type the name of the project (currently `pokedoku2-backend`)
- To deploy to prod manually: `vercel --prod`

# Frontend (GitHub pages)
- Navigate to `frontend`
- Copy `.env` and rename it to `.env.production`
- Under `VITE_BACKEND_URL`, fill in `https://<name_of_host>/`
- To deploy to prod manually:
```
npm run build
npm run deploy
```
Now, you can go to `https://<github-username>.github.io/pokedoku2/` and see your website.