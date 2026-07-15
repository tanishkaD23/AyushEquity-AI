# Database Report

## Project

AyushEquity AI

---

## Database

SQLite

---

## Tables

1. Beneficiaries

2. Hospitals

3. Claims

4. Blockchain_Transactions

---

## Relationships

Beneficiaries

↓

Claims

↑

Hospitals

↓

Blockchain Transactions

---

## Primary Keys

Beneficiary_ID

Hospital_ID

Claim_ID

Transaction_ID

---

## Foreign Keys

Claims.Beneficiary_ID

Claims.Hospital_ID

Blockchain_Transactions.Claim_ID

---

## Record Counts

Beneficiaries : 10000

Hospitals : 500

Claims : 50000

Blockchain : 100

---

## Purpose

Store all project data for AI, Blockchain, APIs and Dashboard.