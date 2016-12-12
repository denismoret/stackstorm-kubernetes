from lib import k8s

from st2actions.runners.pythonrunner import Action


class {{ operationId }}(Action):

    def run(self{% if paramsreq|length > 0 %}, {% endif %} {%- for parameter in paramsreq %}
      {{- parameter.name -}}{%- if not loop.last %}, {% endif -%}
    {% endfor -%} 
    {%- if params|length > 0 %}, {% endif -%}
    {% for parameter in params -%} 
      {{ parameter.name -}}=None{%- if not loop.last %}, {% endif -%}
    {% endfor -%} 
    ):

        myk8s = k8s.K8sClient(self.config)

        args = {}
        {% for p in paramsreq %}
        if {{ p.name }} is not None:
            args['{{ p.name }}'] = {{ p.name }}
        else:
            return (False, "{{ p.name }} is a required parameter")
        {% endfor %}
        {% for p in params %}
        if {{ p.name }} is not None:
            args['{{ p.name }}'] = {{ p.name }}
        {% endfor %}

        return (True, myk8s.runAction('{{ operationId }}', **args))
