from wtforms import SelectField, SelectMultipleField


def _add_chosen_class(kwargs):
    '''
    Add the class 'chosen-select' to the HTML elements, keeping any
    other specified render parameters or other classes.
    '''
    if 'render_kw' in kwargs:
        if 'class' in kwargs['render_kw']:
            kwargs['render_kw']['class'] += ' chosen-select'
        else:
            kwargs['render_kw']['class'] = 'chosen-select'
    else:
        kwargs['render_kw'] = {'class': 'chosen-select'}


class ChosenSelectField(SelectField):
    '''A select field rendered with chosen'''

    def __init__(self, *args, **kwargs):
        _add_chosen_class(kwargs)
        super(ChosenSelectField, self).__init__(*args, **kwargs)


class ChosenSelectMultipleField(SelectMultipleField):
    '''A multiple-select field rendered with chosen'''

    def __init__(self, *args, **kwargs):
        _add_chosen_class(kwargs)
        super(ChosenSelectMultipleField, self).__init__(*args, **kwargs)
