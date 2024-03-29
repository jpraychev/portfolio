temp


{% for post in all_posts %}
    <img src="{{ post.header_image.url }}">
        <p> {{ post.title }} by {{ post.author }} </p>
        <p><a href = "{% url 'post-detail' post.id %}"> {{ post.content }} </a></p>
        <p> Tags: 
            {% for tag in post.tags.all %}
                <a href = " {% url 'tag-view-cbv' tag.name %}"> {{ tag }}</a>
        {% endfor %}
        </p>
        <p>Posted {{ post.time_created_before }} in 
            <a href = " {% url 'cat-view-cbv' post.category %} "> {{ post.category }}  </a> 
        </p>
    </br>
        
    {% endfor %}
    <div class="pagination">
        <span class="step-links">
            {% if page_obj.has_previous %}
                <!-- Arrows -->
                <a href="?page=1">&laquo; first</a>
                <a href="?page={{ page_obj.previous_page_number }}">previous</a>

                <!-- Numbers -->
                <a href="?page=1">1</a>
                <a href="?page=2">2</a>
                <span> ... </span>
            {% endif %}
            
            {% for num in page_obj.paginator.page_range %}
                {% if page_obj.number == num %}
                    <a href = "?page={{num}}"> {{ num }} </a>
                {% elif num > page_obj.number|add:'-2' and num < page_obj.number|add:'2' %}
                    <a href = "?page={{num}}"> {{ num }} </a>
                {% endif %}
            {% endfor %}
            
            
            {% if page_obj.has_next %}
                <span> ... </span>
                <!-- Numbers -->
                <a href="?page={{ page_obj.paginator.num_pages }}"> {{ page_obj.paginator.num_pages|add:'-1' }} </a>
                <a href="?page={{ page_obj.paginator.num_pages }}"> {{ page_obj.paginator.num_pages }} </a>
                <!-- Arrows -->
                <a href="?page={{ page_obj.next_page_number }}">next</a>
                <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
            {% endif %}
        </span>
        </br>
        <span class="current">
            Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
        </span>
    </div> -->