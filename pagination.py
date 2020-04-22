{% if is_paginated %} 
  {% if page_obj.has_previous %}
  <a class="btn btn-outline-info mb-4" href="?page=1">First</a>
  <a
    class="btn btn-outline-info mb-4"
    href="?page={{ page_obj.previous_page_number }}"
    >Previous</a
  >
  {% endif %} 
  {% for num in page_obj.paginator.page_range %} 

      {% if page_obj.number== num %}
      <a class="btn btn-info mb-4" href="?page={{ num }}">{{ num }}</a>
      {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
      <a class="btn btn-outline-info mb-4" href="?page={{ num }}">{{ num }}</a>
      {% endif %} 
  {% endfor %} 
  {% if page_obj.has_next %}
  <a
    class="btn btn-outline-info mb-4"
    href="?page={{ page_obj.next_page_number }}"
    >Next</a
  >
  <a
    class="btn btn-outline-info mb-4"
    href="?page={{ page_obj.paginator.num_pages }}"
    >Last</a
  >
  {% endif %}
{% endif %}