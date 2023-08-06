def get_data_fig(*args, **kwargs):
    return (sum(args), ) + tuple(kwargs[n] for n in ['type', 'color', 'closed', 'width'] if n in kwargs)
