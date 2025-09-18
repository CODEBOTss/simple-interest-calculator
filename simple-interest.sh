#!/bin/bash
# Simple Interest Calculator in Bash

echo "Enter the Principal amount:"
read P

echo "Enter the Rate of Interest (%):"
read R

echo "Enter the Time (in years):"
read T

SI=$((P * R * T / 100))
TOTAL=$((P + SI))

echo "Simple Interest = $SI"
echo "Total Amount = $TOTAL"
