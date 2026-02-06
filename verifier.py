def verify_results(results):
    """
    Verifies execution results.
    Checks if any tool returned an error.
    """

    errors = []

    for result in results:
        output = result.get("output")

        if isinstance(output, dict) and output.get("error"):
            errors.append({
                "tool": result["tool"],
                "error": output["error"]
            })

    if errors:
        return {
            "status": "failed",
            "errors": errors
        }

    return {
        "status": "success",
        "results": results
    }
