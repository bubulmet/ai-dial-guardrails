import asyncio

# from task.t1.no_grounding import main
# if __name__ == "__main__":
#     asyncio.run(main())

# from task.t2.input_api_based import main
# if __name__ == "__main__":
#     main()

# from task.t2.input_vector_based import main
# if __name__ == "__main__":
#     asyncio.run(main())

from task.t3.in_out_grounding import main
if __name__ == "__main__":
    asyncio.run(main())

# Start the user service: docker-compose up -d
# python starter.py
