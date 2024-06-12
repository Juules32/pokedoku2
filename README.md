# Hello!
PokeDoku2 is a personal project of mine, which is a clone of the popular site [PokeDoku](https://pokedoku.com/). It seemed like a nice challenge to work with a backend and a frontend to create a nice, simple application. I also wanted to learn how to host an app for everyone to use, and it has been a nice learning experience for me.

A big help for this project is the publicly available [pokeAPI](https://pokeapi.co/), which helped tremendously with querying and storing all the necessary pokemon data used to generate new daily grids.

The frontend is written in Vite + Vue + TypeScript + Tailwind, and the backend is written in Python + FastAPI.

# How to run locally
## Backend
- Start a new terminal instance and navigate to the `backend` folder.
- Run the following commands:
```
pip install -r requirements.txt
uvicorn main:app --reload --port 80
```

## Frontend
- Start a new terminal instance and navigate to the `frontend` folder.
- Copy the file: `.env.example`, and rename it to `.env.development`.
- Under `VITE_BACKEND_URL`, fill in `http://localhost/`
- Run the following commands:
```
npm i
npm run dev
```

Finally, go to [localhost:5173/pokedoku2/](http://localhost:5173/pokedoku2/).
