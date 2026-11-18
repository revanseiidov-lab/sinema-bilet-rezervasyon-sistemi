CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL CHECK (length(trim(title, char(9, 10, 13, 32))) > 0),
    genre TEXT NOT NULL CHECK (length(trim(genre, char(9, 10, 13, 32))) > 0),
    duration_minutes INTEGER NOT NULL
        CHECK (typeof(duration_minutes) = 'integer' AND duration_minutes > 0),
    description TEXT NOT NULL CHECK (length(trim(description, char(9, 10, 13, 32))) > 0),
    release_year INTEGER NOT NULL
        CHECK (typeof(release_year) = 'integer' AND release_year BETWEEN 1888 AND 2100),
    UNIQUE (title, release_year)
);
