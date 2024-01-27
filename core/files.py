import pandas as pd
from fastapi import Response

def download_data_as_file(data, filename):
    # Use pandas to create a DataFrame and convert it to CSV
    df = pd.DataFrame(data)
    response_content = df.to_csv(index=False)

    return Response(
        content=response_content,
        media_type="text/csv",
        headers={
            "Content-Type": "text/csv",
            "Content-Disposition": f'attachment; filename="{filename}"',
        },
    )