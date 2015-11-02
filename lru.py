#!/usr/bin/env python3
import time
import unittest
import heapq

class CacheEntry:
    def __init__(self, key, value):
        self.timestamp = time.time()
        self.key = key
        self.value = value
        self.removed = False

    def touch(self):
        self.timestamp = time.time()

    def __lt__(self, other):
        return self.timestamp < other.timestamp

    def __repr__(self):
        return 'key= ' + str(self.key) + ', value= ' + str(self.value) + ', timestamp= ' + str(self.timestamp)

class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.heap = []
        self.d = {}

    def put(self, key, val):
        """ O(log(n)) if we are at capacity O(1) otherwise """
        new_entry = CacheEntry(key, val)
        if self.capacity == len(self.heap):
            # evict one and push one
            removed_entry = heapq.heapreplace(self.heap, new_entry)
            self.d.pop(removed_entry.key)
            self.d[key] = new_entry
        else:
            # just add to end of heap
#            heapq.heappush(self.heap, new_entry)
            self.heap.append(new_entry)
            self.d[key] = new_entry

        #print('heap after put=', str(self.heap))

    def get(self, key):
        """ O(n) for the heapify """
        if key in self.d:
            entry = self.d[key]
            entry.touch()
            heapq.heapify(self.heap)
            return entry.value
        else:
            return None

    def _siftup(self, heap, pos):
        endpos = len(heap)
        startpos = pos
        newitem = heap[pos]
        # Bubble up the smaller child until hitting a leaf.
        childpos = 2*pos + 1    # leftmost child position
        while childpos < endpos:
            # Set childpos to index of smaller child.
            rightpos = childpos + 1
            if rightpos < endpos and not cmp_lt(heap[childpos], heap[rightpos]):
                childpos = rightpos
            # Move the smaller child up.
            heap[pos] = heap[childpos]
            pos = childpos
            childpos = 2*pos + 1
        # The leaf at pos is empty now.  Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        heap[pos] = newitem
        _siftdown(heap, startpos, pos)


class Test(unittest.TestCase):
   def testSimple(self):
       c = Cache(2)
       c.put('1', 'A')
       c.put('2', 'B')

       self.assertEqual(c.get('1'), 'A')
       self.assertEqual(c.get('2'), 'B')

   def testEviction(self):
       c = Cache(2)
       c.put('1', 'A')
       c.put('2', 'B')

       self.assertEqual(c.get('1'), 'A')
       self.assertEqual(c.get('2'), 'B')

       c.put('3', 'C')
       self.assertEqual(c.get('3'), 'C')
  
       # key '1' should have been evicted after putting in '3'->'C'
       self.assertEqual(c.get('1'), None)

   def testGetRefreshes(self):
       c = Cache(2)
       c.put('1', 'A')
       c.put('2', 'B')

       self.assertEqual(c.get('2'), 'B')
       self.assertEqual(c.get('1'), 'A')

       c.put('3', 'C')
       self.assertEqual(c.get('3'), 'C')
  
       # key '2' should have been evicted after putting in '3'->'C'
       self.assertEqual(c.get('2'), None)

   def testPutSameThingRefreshes(self):
       pass


if __name__ == '__main__':
    unittest.main()
