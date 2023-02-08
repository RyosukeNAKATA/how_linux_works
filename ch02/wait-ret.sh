#!/bin/bash
false &
wait $! # wait for process end
echo "finish false command: $?"
