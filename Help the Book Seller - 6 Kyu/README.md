<h3>Help the Book Seller - 6 kyu</h3>

<div class="twelve columns phn"><div class="leaderboards-container"><div class="panel is-darkened"><div class="markdown" id="description"><p>A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. Each book has a code c of
  3, 4, 5 or more capitals letters. The 1st letter of a code is the capital letter of the book category.
  In the bookseller's stocklist each code c is followed by a space and by a positive integer n (int n &gt;= 0) 
  which indicates the quantity of books of this code in stock.</p>
<p>For example an extract of one of the stocklists could be:</p>
<pre><code>L = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}.</code></pre><p>or</p>
<pre><code>L = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"] or ....</code></pre><p>  You will be given a stocklist (e.g. : L) and a list of categories in capital letters 
  e.g : </p>
<pre><code>  M = {"A", "B", "C", "W"} </code></pre><p>  or</p>
<pre><code>  M = ["A", "B", "C", "W"] or ...</code></pre><p>  and your task is to find all the books of L with codes 
  belonging to each category of M and to sum their quantity according to each category. </p>
<p>  For the lists L and M of example you have to return the string (in Haskell/Clojure/Racket a list of pairs):  </p>
<pre><code>  (A : 20) - (B : 114) - (C : 50) - (W : 0)</code></pre><p>  where A, B, C, W are the categories, 20 is the sum of the unique book of category A, 114 the sum corresponding
  to "BKWRK" and "BTSQZ", 50 corresponding to "CDXEF" and 0 to category 'W' since there are no code beginning with W.</p>
<p>  If L or M are empty return string is <code>""</code> (Clojure and Racket should return an empty array/list instead).</p>
<h2 id="note">Note:</h2>
<p>In the result codes and their values are in the same order as in M.</p>
</div><div class="mtm"><span><i class="icon-moon-tag "></i></span>
