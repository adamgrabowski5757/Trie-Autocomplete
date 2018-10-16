import sys

class MyTrieNode:
  
    def __init__(self, isRootNode):
        self.isRoot = isRootNode 
        self.isWordEnd = False # is this node a word ending node
        self.isRoot = False # is this a root node
        self.count = 0 # frequency count
        self.next = {} # Dictionary mapping each character from a-z to 
                       # the child node if any corresponding to that character.
        self.words = []   # list of words in tree

    
    ## Function to add words into Trie structure
    def addWord(self,w):
        assert(len(w) > 0)
        cursor = self
        count = 1
        for i in range(len(w)):
            
            # First ever letter in tree
            if cursor.next == {} and i == 0:
                tempnode = MyTrieNode(False)
                cursor.next.update({w[i]:tempnode})
                cursor = cursor.next[w[0]]
                
            elif i == 0 and w[0] in cursor.next:
                cursor = cursor.next[w[0]]
                continue
                
            # This letter is already in the tree at this position
            elif w[i] in cursor.next:
                cursor = cursor.next[w[i]]
                if i == len(w)-1:
                    
                    cursor.isWordEnd = True
                    cursor.count = count
                
                    if w in self.words:
                        cursor.count = cursor.count + 1
                    self.words.append(w)
                    return
                continue
            
            # This letter has yet to be added
            elif w[i] not in cursor.next:
                tempnode = MyTrieNode(False)
                cursor.next.update({w[i]:tempnode})
                cursor = cursor.next[w[i]]
            
            # if we reach end of the word
            if i == len(w)-1:
                cursor.isWordEnd = True
                cursor.count = count
                if w in self.words:
                    cursor.count = cursor.count + 1
                self.words.append(w)
                return
          
        return 
    
    ## Function to look up if a word occurs in current Trie.
    ## Return frequency of occurrence of the word w in the Trie
    ## returns a number for the frequency and 0 if the word w does not occur.
    def lookupWord(self,w):
        
        cursor = self
        tempstring = ""
        for i in range(len(w)):
            if w[i] in cursor.next:
                cursor = cursor.next[w[i]]
                tempstring = tempstring + w[i]
            elif w[i] not in cursor.next:
                return 0
        if tempstring == w:
            return cursor.count
        else: 
            return 0
    
    ## Function to traverse Trie
    ## Used in AutoComplete function
    def traversal(self, cursor, lyst, tempstring):
        if cursor.next == {} and cursor.isWordEnd == True:
            lyst.append((tempstring, cursor.count))
            return tempstring
        elif cursor.isWordEnd == True:
            lyst.append((tempstring, cursor.count))
        
        for x in cursor.next:
            self.traversal(cursor.next[x], lyst, tempstring+x)
        return
    

    ## autoComplete function.
    ## Returns possible list of autocompletions of the word w
    ## Returns a list of pairs (s,j) denoting that
    ## word s occurs with frequency j
    def autoComplete(self,w):
        
        cursor = self
        lyst = []
        tempstring = ""
        # first go through the letters provided
        for i in range(len(w)):    
            if w[i] in cursor.next:
                tempstring = tempstring + w[i]
                cursor = cursor.next[w[i]]
            elif w[i] not in cursor.next:
                lyst = []
                return lyst
        
        # now, start going through all the children from here
        self.traversal(cursor, lyst, tempstring)
        return lyst
    
    