#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Justin Phillips'


class Node:
    def __init__(self, key, value=None):
        """Class initializer."""
        self.key = key
        self.value = value
        self.hash = hash(self.key)

    def __repr__(self):
        """Returns a human-readable representation of key/value contents."""
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):  
        """Compares itself to other Node objects."""
        if self.key == other.key:
            return True
        else:
            return False


class NoDict:
    def __init__(self, num_buckets=10):
        """Class initializer to create the buckets according to a size parameter."""
        self.buckets = [[] for _ in range(num_buckets)]
        self.size = num_buckets

    def __repr__(self):
        """String representation of the contents of the buckets."""
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i, bucket in enumerate(self.buckets)])


    def add(self, key, value=None):
        """This method accepts a new key and value, 
        and store it into the NoDict instance."""
        added_node = Node(key, value)
        bucket = self.buckets[added_node.hash % self.size]
        for key_value in bucket:
            if key_value == added_node:
                bucket.remove(key_value)
                break
        bucket.append(added_node)

    def get(self, key):
        """This method should perform a key-lookup in the NoDict class."""
        key_value = Node(key)
        bucket = self.buckets[key_value.hash % self.size]
        for v in bucket:
            if v == key_value:
                return v.value
        raise KeyError(f'{key} not found')

    def __getitem__(self, key):
        """Enables square-bracket reading behavior."""
        value = self.get(key)
        return value

    def __setitem__(self, key, value):
        """Enables square-bracket assignment behavior."""
        self.add(key, value)