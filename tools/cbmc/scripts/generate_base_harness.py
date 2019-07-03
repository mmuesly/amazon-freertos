
import os
import textwrap
from string import Template

methods_covered = [
    "xQueueGenericReset",
    "xQueueGenericCreateStatic",
    "xQueueGenericCreate",
    "xQueueCreateMutex",
    "xQueueCreateMutexStatic",
    "xQueueGetMutexHolder",
    "xQueueGetMutexHolderFromISR",
    "xQueueGiveMutexRecursive",
    "xQueueTakeMutexRecursive",
    "xQueueCreateCountingSemaphoreStatic",
    "xQueueCreateCountingSemaphore",
    "xQueueGiveFromISR",
    "xQueueSemaphoreTake",
    "xQueueGenericSendFromISR",
    "xQueueGenericSend",
    "prvUnlockQueue",
    "prvCopyDataToQueue",
    "prvNotifyQueueSetContainer",
    "xQueuePeek",
    "xQueueReceive",
    "xQueueReceiveFromISR",
    "uxQueueMessagesWaiting",
    "uxQueueSpacesAvailable",
]

#Eventually I need to do prvIsQueueEmpty explicitly...

methods_to_cover = [
    "xQueueGenericReset",
    "xQueueGenericCreateStatic",
    "xQueueGenericCreate",
    "xQueueCreateMutex",
    "xQueueCreateMutexStatic",
    "xQueueGetMutexHolder",
    "xQueueGetMutexHolderFromISR",
    "xQueueGiveMutexRecursive",
    "xQueueTakeMutexRecursive",
    "xQueueCreateCountingSemaphoreStatic",
    "xQueueCreateCountingSemaphore",
    "xQueueGenericSend",
    "xQueueGenericSendFromISR",
    "xQueueGiveFromISR",
    "xQueueReceive",
    "xQueueSemaphoreTake",
    "xQueuePeek",
    "xQueueReceiveFromISR",
    "uxQueueMessagesWaiting",
    "uxQueueSpacesAvailable",
    "uxQueueMessagesWaitingFromISR",
    "vQueueDelete",
    "uxQueueGetQueueNumber",
    "vQueueSetQueueNumber",
    "ucQueueGetQueueType",
    "xQueueIsQueueEmptyFromISR",
    "xQueueIsQueueFullFromISR",
    "xQueueCRSend",
    "xQueueCRReceive",
    "xQueueCRSendFromISR",
    "xQueueCRReceiveFromISR",
    "vQueueAddToRegistry",
    "pcQueueGetName",
    "vQueueUnregisterQueue",
    "vQueueWaitForMessageRestricted",
    "xQueueCreateSet",
    "xQueueAddToSet",
    "xQueueRemoveFromSet",
    "xQueueSelectFromSet",
    "xQueueSelectFromSetFromISR",
    "xQueuePeekFromISR"
]

method_parameter = {}
method_parameter["xQueueGenericReset"] = [
    ("QueueHandle_t", "xQueue"),
    ("BaseType_t", "xNewQueue")]
method_parameter["xQueueGenericCreateStatic"] = [
    ("UBaseType_t", "uxQueueLength"),
    ("UBaseType_t", "uxItemSize"),
    ("uint8_t", "*pucQueueStorage"),
    ("StaticQueue_t", "*pxStaticQueue"),
    ("uint8_t", "ucQueueType")
]
method_parameter["xQueueCreateMutex"] = [
    ("uint8_t", "ucQueueType")
]
method_parameter["xQueueCreateMutexStatic"] = [
    ("uint8_t", "ucQueueType"),
    ("StaticQueue_t", "*pxStaticQueue")
]

method_parameter["xQueueGetMutexHolder"] = [
    ("QueueHandle_t", "xSemaphore")
]

method_parameter["xQueueGetMutexHolderFromISR"] = [
    ("QueueHandle_t", "xSemaphore")
]

method_parameter["xQueueGiveMutexRecursive"] = [
    ("QueueHandle_t", "xMutex")
]

method_parameter["xQueueTakeMutexRecursive"] = [
    ("QueueHandle_t", "xMutex"),
    ("TickType_t", "xTicksToWait")]

method_parameter["xQueueCreateCountingSemaphoreStatic"] = [
    ("UBaseType_t", "uxMaxCount"),
    ("UBaseType_t", "uxInitialCount"),
    ("StaticQueue_t", "*pxStaticQueue")
]

method_parameter["xQueueCreateCountingSemaphore"] = [
    ("UBaseType_t", "uxMaxCount"),
    ("UBaseType_t", "uxInitialCount")
]

method_parameter["xQueueGenericSend"] = [
    ("QueueHandle_t", "xQueue"),
    ("void", "*pvItemToQueue"),
    ("TickType_t", "xTicksToWait"),
    ("BaseType_t", "xCopyPosition")
]

method_parameter["xQueueGenericSendFromISR"] = [
    ("QueueHandle_t", "xQueue"),
    ("void", "*pvItemToQueue"),
    ("BaseType_t", "*pxHigherPriorityTaskWoken"),
    ("BaseType_t", "xCopyPosition")
]

method_parameter["xQueueGiveFromISR"] = [
    ("QueueHandle_t", "xQueue"),
    ("BaseType_t", "*pxHigherPriorityTaskWoken")
]

method_parameter["xQueueReceive"] = [
    ("QueueHandle_t", "xQueue"),
    ("void", "*pvBuffer"),
    ("TickType_t", "xTicksToWait")
]

method_parameter["xQueueSemaphoreTake"] = [
    ("QueueHandle_t", "xQueue"),
    ("TickType_t", "xTicksToWait")
]

method_parameter["xQueuePeek"] = [
    ("QueueHandle_t", "xQueue"),
    ("void", "*pvItemToQueue"),
    ("TickType_t", "xTicksToWait")
]

method_parameter["xQueueReceiveFromISR"] = [
    ("QueueHandle_t", "xQueue"),
    ("void", "*pvBuffer"),
    ("BaseType_t", "*pxHigherPriorityTaskWoken")
]

method_parameter["xQueuePeekFromISR"] = [
    ("QueueHandle_t", "xQueue"),
    ("void", "*pvBuffer")
]

method_parameter["uxQueueMessagesWaiting"] = [
    ("QueueHandle_t", "xQueue")
]

method_parameter["uxQueueSpacesAvailable"] = [
    ("QueueHandle_t", "xQueue")
]

method_parameter["uxQueueMessagesWaitingFromISR"] = [
    ("QueueHandle_t", "xQueue")
]

method_parameter["vQueueDelete"] = [
    ("QueueHandle_t", "xQueue")
]

method_parameter["uxQueueGetQueueNumber"] = [
    ("QueueHandle_t", "xQueue")
]

method_parameter["vQueueSetQueueNumber"] = [
    ("QueueHandle_t", "xQueue")
]

method_parameter["ucQueueGetQueueType"] = [
    ("QueueSetHandle_t", "xQueueSet")
]

method_parameter["xQueueIsQueueEmptyFromISR"] = [
    ("QueueHandle_t", "xQueue")
]

method_parameter["xQueueIsQueueFullFromISR"] = [
    ("QueueHandle_t", "xQueue")
]

method_parameter["xQueueCRSend"] = [
    ("QueueHandle_t", "xQueue"),
    ("void", "*pvItemToQueue"),
    ("TickType_t", "xTicksToWait")
]

method_parameter["xQueueCRReceive"] = [
    ("QueueHandle_t", "xQueue"),
    ("void", "*pvBuffer"),
    ("TickType_t", "xTicksToWait")
]

method_parameter["xQueueCRSendFromISR"] = [
    ("QueueHandle_t", "xQueue"),
    ("void", "*pvItemToQueue"),
    ("BaseType_t", "xCoRoutinePreviouslyWoken")
]

method_parameter["xQueueCRReceiveFromISR"] = [
    ("QueueHandle_t", "xQueue"),
    ("void", "*pvBuffer"),
    ("BaseType_t", "*xCoRoutineWoken")
]

method_parameter["vQueueAddToRegistry"] = [
    ("QueueHandle_t", "xQueue"),
    ("char", "*pcQueueName"),
]

method_parameter["pcQueueGetName"] = [
    ("QueueHandle_t", "xQueue")
]

method_parameter["vQueueUnregisterQueue"] = [
    ("QueueHandle_t", "xQueue")
]

method_parameter["vQueueWaitForMessageRestricted"] = [
    ("QueueHandle_t", "xQueue"),
    ("TickType_t", "xTicksToWait"),
    ("BaseType_t", "xWaitIndefinitely")
]

method_parameter["xQueueCreateSet"] = [
    ("UBaseType_t", "uxEventQueueLength")
]

method_parameter["xQueueAddToSet"] = [
    ("QueueSetMemberHandle_t", "xQueueOrSemaphore"),
    ("QueueSetHandle_t", "xQueueSet")
]

method_parameter["xQueueRemoveFromSet"] = [
    ("QueueSetMemberHandle_t", "xQueueOrSemaphore"),
    ("QueueSetHandle_t", "xQueueSet")
]

method_parameter["xQueueSelectFromSet"] = [
    ("QueueSetHandle_t", "xQueueSet"),
    ("TickType_t", "xTicksToWait")
]

method_parameter["xQueueSelectFromSetFromISR"] = [
    ("QueueSetHandle_t", "xQueueSet")
]

HARNESS_TEMPLATE = Template(textwrap.dedent("""\
    #include "FreeRTOS.h"
    #include "queue.h"
    #include "queue_init.h"

    #include "cbmc.h"


    void harness(){
        $parameter_declaration

        $method_call
    }
    """))

MAKEFILE_JSON_TEMPLATE = Template(textwrap.dedent("""\
    {
      "ENTRY": "$entry",
      "CBMCFLAGS": [
        "--unwind 1",
        "--signed-overflow-check",
        "--pointer-overflow-check",
        "--unsigned-overflow-check",
        "--nondet-static"
      ],
      "OBJS": [
        "$$(ENTRY)_harness.goto",
        "$$(FREERTOS)/freertos_kernel/queue.goto",
        "$$(FREERTOS)/freertos_kernel/list.goto"
      ],
      "DEF": [
        "'mtCOVERAGE_TEST_MARKER()=__CPROVER_assert(1, \"Coverage marker\")'",
        "configUSE_TRACE_FACILITY=0",
        "configGENERATE_RUN_TIME_STATS=0",
        "configSUPPORT_STATIC_ALLOCATION=1",
        "configSUPPORT_DYNAMIC_ALLOCATION=1"
      ],
      "INC": [
        "."
      ],
      "GENERATE_HEADER": [
        "queue_datastructure.h"
      ]
    }
    """))

def declare_parameter(param_tuple):
    param_name = param_tuple[1]
    if param_name.startswith("*p") and param_tuple[0] != "void":
        param_name = param_name[2:]

    if param_tuple[0] == "QueueHandle_t":
        return textwrap.dedent("""\
              QueueHandle_t {} =
                  xUnconstrainedQueue();
            """.format(param_name))
    else:
        return "{} {};".format(param_tuple[0], param_name)

def parameter_declarations(method):
    declarations = []
    for parameter in method_parameter[method]:
        declarations.append(declare_parameter(parameter))
    return "\n    ".join(declarations)

def method_call_content(method):
    parameters = []
    for parameter in method_parameter[method]:
        param_name = parameter[1]
        if param_name.startswith("*p") and parameter[0] != "void":
            param_name = "&" + param_name[2:]
        if param_name.startswith("*"):
            param_name = param_name[1:]
        parameters.append(param_name)

    parameters = ", ".join(parameters)
    return "{}( {} );".format(method, parameters)


def generate_remaining():
    queue_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                "..", "proofs", "Queue")
    for method in methods_to_cover:
        print(method)
        if method not in methods_covered:

            if method[1] == 'Q':
                method_name = method[1:]
            else:
                method_name = method[2:]
            harness_file = method_name + "_harness.c"
            makefile_json = "Makefile.json"
            target_folder = os.path.join(queue_folder, method_name)
            os.makedirs(target_folder, exist_ok=True)
            parameter_declaration = parameter_declarations(method)
            method_call = method_call_content(method)

            with open(os.path.join(target_folder, harness_file), "w") as harness:
                print(HARNESS_TEMPLATE.substitute(
                    parameter_declaration=parameter_declaration,
                    method_call=method_call), file=harness)

            with open(os.path.join(target_folder, makefile_json), "w") as makefile:
                print(MAKEFILE_JSON_TEMPLATE.substitute(entry=method_name),
                      file=makefile)


def main():
    print("done:", len(methods_covered), "/", len(methods_to_cover), "(", len(methods_covered)/len(methods_to_cover), "%)")

if __name__ == '__main__':
    generate_remaining()
    main()
