-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS program;

CREATE TABLE program (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  code TEXT NOT NULL,
  url TEXT NOT NULL UNIQUE
);
