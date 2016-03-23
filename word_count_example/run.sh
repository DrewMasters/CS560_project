#!/bin/bash

yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -files mapper_inverted_index.py,reducer_inverted_index.py -mapper mapper_inverted_index.py -reducer reducer_inverted_index.py -input wasb:///example/shakespeare_ln2.txt -output wasb:///example/wordcountout_final
