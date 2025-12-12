def run_stage(stage):
    print(f"Running stage: {stage}")
    # placeholder routing
    if stage=="ocr":
        pass
    elif stage=="preprocess":
        pass
    elif stage=="train_lstm":
        pass
    elif stage=="all":
        pass

if __name__=="__main__":
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument("--stage")
    args=p.parse_args()
    run_stage(args.stage)
