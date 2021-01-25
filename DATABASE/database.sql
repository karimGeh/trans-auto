CREATE TABLE rfid_cards (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    code VARCHAR(50) NOT NULL UNIQUE,
    x BIGINT NOT NULL,
    y BIGINT NOT NULL
);

CREATE TABLE links (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    first_end BIGINT REFERENCES rfid_cards(id),
    second_end BIGINT REFERENCES rfid_cards(id)
);