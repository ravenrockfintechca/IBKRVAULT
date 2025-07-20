def rotate_strategies(context, score_dict):
    # rank strategies by score and select top N
    return sorted(score_dict.items(), key=lambda x: -x[1])[:context['top_n']]