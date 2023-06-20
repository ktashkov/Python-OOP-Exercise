from typing import List
from project.hardware import Hardware, HeavyHardware, PowerHardware
from project.software import Software, ExpressSoftware, LightSoftware


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        hw = PowerHardware(name, capacity, memory)
        System._hardware.append(hw)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hw = HeavyHardware(name, capacity, memory)
        System._hardware.append(hw)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hw = next((hw for hw in System._hardware if hw.name == hardware_name), None)
        if hw is None:
            return "Hardware does not exist"
        sw = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hw.install(sw)
            System._software.append(sw)
        except Exception as e:
            raise Exception("Software cannot be installed") from e

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hw = next((hw for hw in System._hardware if hw.name == hardware_name), None)
        if hw is None:
            return "Hardware does not exist"
        sw = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hw.install(sw)
            System._software.append(sw)
        except Exception as e:
            raise Exception("Software cannot be installed") from e

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hw = next((hw for hw in System._hardware if hw.name == hardware_name), None)
        sw = next((sw for sw in System._software if sw.name == software_name), None)
        if hw is None or sw is None or sw not in hw.software_components:
            return "Some of the components do not exist"
        hw.uninstall(sw)
        System._software.remove(sw)

    @staticmethod
    def analyze():
        total_memory_consumption = sum(sw.memory_consumption for sw in System._software)
        total_memory = sum(hw.memory for hw in System._hardware)
        total_capacity_consumption = sum(sw.capacity_consumption for sw in System._software)
        total_capacity = sum(hw.capacity for hw in System._hardware)
        return f"System Analysis\nHardware Components: {len(System._hardware)}\nSoftware Components:" \
               f" {len(System._software)}\nTotal Operational Memory: " \
               f"{total_memory_consumption} / {total_memory}\nTotal Capacity Taken: " \
               f"{total_capacity_consumption} / {total_capacity}"

    @staticmethod
    def analyze():
        total_memory_consumption = sum(s.memory_consumption for s in System._software)
        total_hardware_memory = sum(h.memory for h in System._hardware)
        total_capacity_consumption = sum(s.capacity_consumption for s in System._software)
        total_hardware_capacity = sum(h.capacity for h in System._hardware)

        return f"System Analysis\nHardware Components: {len(System._hardware)}\nSoftware Components:" \
               f" {len(System._software)}\nTotal Operational Memory: " \
               f"{total_memory_consumption} / {total_hardware_memory}\nTotal Capacity Taken:" \
               f" {total_capacity_consumption} / {total_hardware_capacity}"

    @staticmethod
    def system_split():
        result = []
        for hardware in System._hardware:
            software_names = [s.name for s in hardware.software_components]
            if len(software_names) == 0:
                software_names = "None"
            else:
                software_names = ", ".join(software_names)

            result.append(
                f"Hardware Component - {hardware.name}\nExpress Software Components:"
                f" {hardware.count_express_software()}\nLight Software Components:"
                f" {hardware.count_light_software()}\nMemory Usage: "
                f"{hardware.get_total_memory_consumption()} / {hardware.memory}\nCapacity Usage: "
                f"{hardware.get_total_capacity_consumption()} / {hardware.capacity}\nType:"
                f" {hardware.hardware_type}\nSoftware Components: {software_names}") return "\n".join(result)

