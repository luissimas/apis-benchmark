import Fastify from "fastify";
import { v4 as uuid } from "uuid";
import { Pool } from "pg";

const port = Number(process.env.PORT) || 3000;
const host = process.env.HOST || "localhost";
const connectionString =
  process.env.DB_URL || "postgresql://postgres:password@localhost:5432/db";

export interface Movie {
  id: string;
  name: string;
  release_date: Date;
  director: string;
  description?: string;
  duration?: number;
  budget?: number;
}

const makeMovies = (): Movie[] => {
  const result: Movie[] = new Array(1000);
  for (let i = 0; i < result.length; i++) {
    result[i] = {
      id: uuid(),
      name: "any-name",
      release_date: new Date(),
      director: "any-director",
      description: "any-description",
      duration: 1000,
      budget: 10000,
    };
  }
  return result;
};

const fastify = Fastify({
  logger: false,
});
const pool = new Pool({ connectionString });

fastify.get("/db", async (req, res) => {
  const result = await pool.query("SELECT * FROM movies LIMIT 20");
  res.send(result.rows);
});
fastify.get("/cache", async (req, res) => {
  const result = makeMovies();
  res.send(result);
});

const run = async () => {
  try {
    await fastify.listen({ port, host });
  } catch (err) {
    fastify.log.error(err);
    process.exit(1);
  }
};

run();
