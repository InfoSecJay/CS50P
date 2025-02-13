-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Get relevant crime scene reports
SELECT * FROM crime_scene_reports WHERE street = "Humphrey Street" AND day = 28 AND month = 7;

-- Get relevant transcripts from witnesses form crime scene report #295
SELECT * FROM interviews WHERE transcript LIKE '%bakery%' AND month = 7 and day = 28;

-- Bakery security footage  for license plate activity around 10AM on the morning of the theft
SELECT * FROM bakery_security_logs WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10;

-- Phone call logs around time of theft under a minute long
SELECT * FROM phone_calls WHERE year = 2023 AND day = 28 AND month = 7 AND duration <= 60;

-- Thief was seen withdrawing money via ATM on Leggett Street on day of crime
SELECT * FROM atm_transactions WHERE atm_location = "Leggett Street" AND day = 28 AND month = 7 AND year = 2023 AND transaction_type = 'withdraw';

-- All flights out of Fiftyville on the 29th
SELECT * FROM flights WHERE year = 2023 AND month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville');


-- List of suspects who were seen at the Bakery around time of theft
SELECT name FROM people WHERE license_plate in (SELECT license_plate FROM bakery_security_logs WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10);

-- List of suspects who made a phone call around time of theft
SELECT name FROM people WHERE phone_number in (SELECT caller FROM phone_calls WHERE year = 2023 AND day = 28 AND month = 7 AND duration <= 60);

-- List of suspects who withdrew money at Leggett Street around time of theft
SELECT name FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE atm_location = "Leggett
Street" AND day = 28 AND month = 7 AND year = 2023 AND transaction_type = 'withdraw'));

-- Suspects for flights departing Fiftyville on the 29th
SELECT * FROM passengers WHERE flight_id IN (SELECT id FROM flights WHERE year = 2023 AND month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville'));

SELECT passport_number FROM passengers WHERE flight_id IN (SELECT id FROM flights WHERE year = 2023 AND month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville'));
