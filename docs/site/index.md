<section class="hero" markdown="0">
<div>
<h1>Know if it's worth building. Then build it right.</h1>
<svg class="line-tick" viewBox="0 0 240 24" aria-hidden="true" focusable="false"><path d="M2 12H202L210 19L228 5"/></svg>
<p class="lead">MakerLine is a free, open-source Claude plugin for designers and solo makers. It turns a few sentences into an honest verdict, real competitors, wireframes and a draft PRD (product requirements document). Once you approve, it helps you build the product with accessibility, security and tests enforced at every step.</p>
<p class="actions"><a class="btn primary" href="five-minutes.md">Try it in 5 minutes</a> <a class="btn" href="#install">Install</a></p>
</div>
<figure class="verdict">
<p class="doc-path">clubslot/docs/product/ONE_PAGER.md</p>
<p class="verdict-line"><span class="stamp">Pivot</span> Medium-low confidence</p>
<dl>
<div><dt>The brief said</dt><dd>"No competitors" for a booking app in gated communities.</dd></div>
<div><dt>Reality check</dt><dd>MyGate, NoBrokerHood and ADDA already bundle booking for about 25,000 communities each.</dd></div>
<div><dt>How to make it stronger</dt><dd>Cut version 1 to fair, no-install booking from a WhatsApp link, and test it with five committees before writing code.</dd></div>
</dl>
<figcaption>From a real Idea Pack run. <a href="case-clubslot.md">Read the ClubSlot case study</a></figcaption>
</figure>
</section>

<section aria-labelledby="how" markdown="0">
<div class="section-intro">
<h2 id="how">From idea to launch, with you in charge</h2>
<p>Every phase is a skill you can run on its own or all at once. The kit stops before any code until you approve the idea, and no AI tool can approve it for you.</p>
</div>
<ol class="track">
<li><h3>Describe the idea</h3><p>A short interview, or just your pitch.</p></li>
<li><h3>Get an honest evaluation</h3><p>A verdict, real competitors, the strongest version and who it leaves out.</p></li>
<li><h3>See it</h3><p>Design direction, clickable wireframes and a draft PRD.</p></li>
<li class="gate"><h3>You approve</h3><p>Nothing is built until you say so.</p></li>
<li><h3>Set it up</h3><p>Name and brand, stack, design system, engineering docs and repo rules.</p></li>
<li><h3>Build, review, ship</h3><p>One task at a time, tests first, reviewed for accessibility and security.</p></li>
</ol>
<p class="track-note">Steps 1–3 give you an Idea Pack. They are also available on their own as <a href="../../makerline-idea/README.md">MakerLine Idea</a>.</p>
</section>

<section aria-labelledby="try" markdown="0">
<h2 id="try">Try it</h2>
<p>Connect an empty folder to a new Claude chat, then type one of these.</p>
<ul class="prompts">
<li><code>/makerline:start give me everything for this idea, quick: a booking app for small physio clinics</code></li>
<li><code>Who are my competitors, and is my differentiator real?</code></li>
<li><code>What would it look like? Show me wireframes.</code></li>
<li><code>Make my tool plan. I have Claude, ChatGPT and Cursor.</code></li>
</ul>
<p>Using the MakerLine Idea plugin? Type <code>/makerline-idea:start</code> instead.</p>
</section>

<section id="install" aria-labelledby="install-h" markdown="0">
<h2 id="install-h">Install</h2>
<div class="two">
<div>
<h3>Claude app, desktop or web</h3>
<ol>
<li>Open <strong>Customize</strong>, then <strong>Plugins</strong>.</li>
<li>Choose <strong>Add marketplace</strong> and enter <code>sairam5294/product-kit</code>.</li>
<li>Install <strong>makerline</strong> or <strong>makerline-idea</strong>, not both.</li>
<li>Turn on <strong>Sync automatically</strong> to get updates.</li>
</ol>
</div>
<div>
<h3>Claude Code</h3>
<pre tabindex="0"><code>claude plugin marketplace add sairam5294/product-kit
claude plugin install makerline@makerline</code></pre>
<p>Check it worked: type <code>/makerline:</code> in a new chat and the skills appear.</p>
</div>
</div>
</section>

<section aria-labelledby="which" markdown="1">
<h2 id="which">MakerLine or MakerLine Idea?</h2>

| | MakerLine Idea | MakerLine |
|---|---|---|
| Best for | Deciding whether an idea is worth building | Building and shipping it once you've decided |
| You get | An Idea Pack: brief, evaluation, competitors, wireframes, draft PRD, one-pager, validation tests | Everything in MakerLine Idea, plus brand, stack, design system, engineering docs, repo setup, build, review, test and ship |
| Writes code | No | Yes, after you approve |
| Needs a terminal | No | Only for building |
| Start with | `/makerline-idea:start` | `/makerline:start` |

Not sure? Start with MakerLine Idea. If you decide to build, switch to MakerLine: your documents stay in your folder and `/makerline:start` picks up where you left off.

</section>

<section aria-labelledby="cases" markdown="0">
<h2 id="cases">See it on real projects</h2>
<div class="cases">
<a class="case" href="case-rhythmbuddy.md"><strong>RhythmBuddy</strong><span>A shipped macOS app adopted into the kit. Four reviewers found 8 must-fix problems in a project that already had 275 passing tests.</span></a>
<a class="case" href="case-clubslot.md"><strong>ClubSlot</strong><span>An Idea Pack run on a brief that claimed "no competitors". The kit found the real ones and recommended a sharper pivot.</span></a>
</div>
</section>

<section aria-labelledby="principles" markdown="0">
<h2 id="principles">Built on three promises</h2>
<div class="three">
<div><h3>Accessible worldwide</h3><p>WCAG 2.2 AA is the floor for everything it makes. Every evaluation asks who the idea leaves out and which accessibility laws apply where you launch.</p></div>
<div><h3>Honest about its mistakes</h3><p>Every blind test and real project is logged in <a href="../../LESSONS.md">what the kit got wrong</a>, and turned into fixes in the <a href="../../CHANGELOG.md">changelog</a>.</p></div>
<div><h3>Your files stay yours</h3><p>Everything it writes is Markdown and HTML in your own folder. No servers of its own, no tracking, no account. <a href="privacy.md">Privacy</a></p></div>
</div>
</section>
