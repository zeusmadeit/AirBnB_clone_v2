class ParserEngine:

    @staticmethod
    def extract_args(args):
        data = {}
        for arg in args:
            if "=" not in arg:
                continue

            key, value = arg.split("=")
            if not key or not value:
                continue

            if value[0] == '"' and value[-1] == '"':
                value = value[1:-1]
                value = value.replace("_", " ")
                data[key] = value
            elif value.isdigit():
                value = int(value)
                data[key] = value
            else:
                try:
                    value = float(value)
                    data[key] = value
                except ValueError:
                    continue
        return data

    @staticmethod
    def parse_create(args: str):
        data = {
            "class_name": None,
            "args": None
        }
        if not args:
            return data

        data_split = args.split(" ")

        data["class_name"] = data_split[0]
        data["args"] = ParserEngine.extract_args(data_split[1:])
        return data
