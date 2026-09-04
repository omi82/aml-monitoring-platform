from app.ai.engine_llm import EngineLLM


def main():

    llm = EngineLLM()

    response = llm.generate(
        "Introduce yourself in one sentence."
    )

    print("\nResponse:\n")
    print(response)


if __name__ == "__main__":
    main()