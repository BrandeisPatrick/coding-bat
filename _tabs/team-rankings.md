---
layout: page
title: Team Rankings
icon: fas fa-trophy
order: 6
excerpt: ""
---

{% for team in site.data.teams.teams %}
  {% assign total = 0 %}
  {% for member in team.members %}
    {% assign total = total | plus: member.rank %}
  {% endfor %}
  {% assign count = team.members | size %}
  {% assign avg = total | plus: 0.0 | divided_by: count %}

### {{ team.name }}

| Member | Rank |
|--------|------|
{% for member in team.members %}
| {{ member.name }} | {{ member.rank }} |
{% endfor %}

**Average Rank:** {{ avg | round: 2 }}

{% endfor %}
