---
layout: page
icon: fas fa-stream
order: 5
title: Timeline
---

<style>
.timeline {
  margin-left: 1rem;
  border-left: 4px solid var(--timeline-color, #c2c6cc);
  padding-left: 1rem;
}
.timeline-item {
  position: relative;
  margin-bottom: 1.25rem;
}
.timeline-item::before {
  content: '';
  position: absolute;
  left: -8px;
  top: 0.25rem;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--timeline-node-bg, #c2c6cc);
}
</style>

<div class="timeline">
  <div class="timeline-item">
    <strong>Software Developer, Example Corp</strong> (2018-2020)
    <p>Worked with an amazing team of peers to build web applications.</p>
  </div>
  <div class="timeline-item">
    <strong>Senior Developer, Sample Inc</strong> (2020-2022)
    <p>Led a group of developers and mentored new teammates.</p>
  </div>
  <div class="timeline-item">
    <strong>Tech Lead, Demo Labs</strong> (2022-Present)
    <p>Guiding cross-functional peers on various projects.</p>
  </div>
</div>
