<h3>Where my anagrams at? - 5 kyu</h3>
https://www.codewars.com/kata/523a86aa4230ebb5420001e1
<p><div class="leaderboards-container"><div class="panel is-darkened"><div class="markdown" id="description"><p>What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:</p>
<pre><code>'abba' &amp; 'baab' == true

'abba' &amp; 'bbaa' == true

'abba' &amp; 'abbba' == false

'abba' &amp; 'abca' == false</code></pre><p>Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:</p>
<pre><code class="language-javascript">anagrams(<span class="hljs-string">'abba'</span>, [<span class="hljs-string">'aabb'</span>, <span class="hljs-string">'abcd'</span>, <span class="hljs-string">'bbaa'</span>, <span class="hljs-string">'dada'</span>]) =&gt; [<span class="hljs-string">'aabb'</span>, <span class="hljs-string">'bbaa'</span>]

anagrams(<span class="hljs-string">'racer'</span>, [<span class="hljs-string">'crazer'</span>, <span class="hljs-string">'carer'</span>, <span class="hljs-string">'racar'</span>, <span class="hljs-string">'caers'</span>, <span class="hljs-string">'racer'</span>]) =&gt; [<span class="hljs-string">'carer'</span>, <span class="hljs-string">'racer'</span>]

anagrams(<span class="hljs-string">'laser'</span>, [<span class="hljs-string">'lazing'</span>, <span class="hljs-string">'lazy'</span>,  <span class="hljs-string">'lacer'</span>]) =&gt; []</code></pre>
</div><div class="mtm"><span><i class="icon-moon-tag "></i></span>
