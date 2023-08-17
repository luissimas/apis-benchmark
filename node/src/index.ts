import Fastify from "fastify";
import { v4 as uuid } from "uuid";
import { Model } from "objection";
import Knex from "knex";

export interface Movie {
  id: string;
  name: string;
  release_date: Date;
  director: string;
  description?: string;
  duration?: number;
  budget?: number;
}

const id = uuid();
const movies: Movie[] = new Array(1000).fill(0).map((_) => ({
  id: uuid(),
  name: "any-name",
  release_date: new Date(),
  director: "any-director",
  description: "any-description",
  duration: 10000,
  budget: 10000,
}));

const knex = Knex({
  client: "pg",
  connection: {
    host: "localhost",
    port: 5432,
    user: "postgres",
    password: "password",
    database: "db",
  },
});
Model.knex(knex);
export class MovieModel extends Model {
  static get tableName() {
    return "movies";
  }

  id: string;
  name: string;
  release_date: Date;
  director: string;
  description?: string;
  duration?: number;
  budget?: number;
}

const fastify = Fastify();
fastify.get("/db", async (req, res) => MovieModel.query().limit(100));
fastify.get("/cache", async (req, res) => res.send(movies));

const run = async () => {
  try {
    await fastify.listen({ port: 3000 });
  } catch (err) {
    fastify.log.error(err);
    process.exit(1);
  }
};

run();
