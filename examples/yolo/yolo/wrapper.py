import os
import json
from surround import Surround, Wrapper, AllowedTypes
from stages import ValidateData, YoloData

class PipelineWrapper(Wrapper):
    def __init__(self):
        surround = Surround([ValidateData()], __name__)
        super().__init__(surround)

    def run(self, input_data):
        text = json.loads(input_data)["data"]
        data = YoloData(text)
        self.surround.process(data)
        return {"output": data.output_data}
