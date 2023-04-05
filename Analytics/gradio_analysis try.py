import gradio
import gradio as gr
import pandas as pd

sample_report = pd.DataFrame(
    {
        'Line': ['CPM', 'CPM', 'FCM', 'FCM', 'CPM Trolley #2', 'CPM', 'BF', 'CPM', 'FCM', 'FEM', 'BF', 'FEM', 'FCM', 'ENG', 'ENG', 'BF', 'FCM', 'BR', 'BF', 'ENG', 'CPM Trolley #1', 'FCM', 'FCM', 'CPM', 'ENG', 'FCM', 'FCM', 'CPM', 'BF', 'BF', 'BR', 'BR', 'BF', 'BF', 'BF', 'RCM', 'RCM', 'FCM', 'ENG', 'CPM', 'CPM', 'ENG', 'ENG', 'BF', 'ENG', 'BF', 'CPM', 'BF', 'ENG', 'RCM', 'ENG', 'ENG', 'FCM', 'RCM', 'FEM', 'BF', 'FEM', 'BF', 'BF', 'FCM Trolley', 'FCM', 'BF', 'BF', 'IP Sub', 'ENG', 'BR', 'RCM', 'ENG', 'FCM Trolley', 'RCM', 'FCM', 'CPM', 'FCM', 'CPM', 'FEM', 'CPM', 'ENG', 'ENG', 'ENG', 'ENG', 'RCM', 'RCM', 'ENG', 'ENG', 'FCM', 'ENG', 'CPM Trolley #1', 'CPM', 'CPM', 'BF', 'FEM', 'FEM', 'CPM', 'ENG', 'FEM', 'BF', 'FEM', 'FCM', 'CPM', 'CPM', 'FEM', 'CPM', 'BF', 'BF', 'FEM', 'BF', 'CPM', 'CPM Trolley #2', 'FCM', 'BF', 'BF', 'CPM', 'BF', 'FEM', 'BF', 'RCM', 'FCM', 'FCM', 'RCM', 'CPM', 'BF', 'FEM', 'ENG', 'BF', 'CPM', 'FEM', 'CPM', 'BR', 'CPM', 'RCM', 'RCM', 'CPM Trolley #1', 'BF', 'FEM', 'BR', 'BR', 'CPM', 'FEM', 'ENG', 'ENG', 'CPM', 'FCM', 'BF', 'FCM', 'CPM', 'RCM', 'BF', 'ENG', 'BR', 'ENG', 'FEM', 'CPM', 'FCM', 'FCM', 'BF', 'CPM', 'ENG', 'FEM', 'IP Sub', 'CPM', 'BF', 'IP Sub', 'CPM', 'FEM', 'FCM Trolley', 'CPM', 'FCM', 'BF', 'BF', 'ENG'],
        'Station': ['QC', '14', 'AGV1', 'Matching', '1', 'IPC', 'CKD', '19', '6', '4', 'Grille Upr CKD(Sub)', '12scc', 'AGV0', 'Matching', 'Matching', '12(QC)', 'Matching', '6', 'Work Printer', 'IPC', 'Printer(66)', '18', '19', '4', 'Matching', '19', '18', 'TBar1', 'IPC', 'Printer(67)', '4', 'ON PE Punch', '8', '3', 'Work Printer', 'IPC', '21', '19', 'Work Printer', 'IPC', '20', 'Matching', 'Matching', 'Shipping Rack', 'IPC', 'Printer(67)', 'IPC', '6', '5', 'IPC', 'Matching', 'IPC', 'Matching', '21', '9', 'Printer(65)', '9', 'OKI(51)', 'Shipping', '2', '19', '12(QC)', 'Printer(65)', 'Matching', 'Work Printer', 'Printer(240)', '20', 'Matching', '1', '21', '19', '17', '8', 'Shipping', '4', 'TBar1', '8', '10', 'IPC', '11', '21', '21', '11', 'Matching', 'IPC', 'Matching', 'Printer(66)', '18', 'IPC', 'Printer(61)', 'Matching', 'Matching', '31', '6', '14', 'Fog(Sub)', '12', 'Matching', '2', '6', '9', '19', 'ON(Sub)', 'ON(Sub)', '14', 'Shipping', 'IPC', '1', '6', 'MQ4a(Sub)', 'UPRCVR(Sub)', '25 Sub', '6', '12SCC', '6', 'Printer(56)', 'Matching', 'Matching', '4', 'IPC', '3', 'QC', '15-1', 'Printer(65)', '4', '12SCC', 'IPC', 'Matching', 'IPC', 'Matching', 'QC', '2', '2', '16', 'ON PE Punch', 'Matching', '30', '5', 'Matching', 'IPC', '27', '8', '2', '10', 'IPC', '10', 'Printer(66)', 'IPC', 'Matching', 'Matching', 'QC', '19', '17', '14', 'Grille Upr CKD(Sub)', '27', 'Storage', '9', 'Feeding', 'IPC', 'Matching', '4', '2', '10', 'Printer(65)', '19', 'Matching', 'Printer(66)', '8', 'Matching'],
        'Device': ['PPC', 'Scanner', 'Printer', 'Scanner', 'Spring Balancer', 'IPC', 'Printer', 'Scanner', 'Scanner', 'Scanner', 'PPC', 'Scanner', 'Printer', 'Scanner', 'Skid', 'Scanner', 'RFID Tag', 'Scanner', 'Printer', 'Skid', 'Printer', 'Scanner', 'Scanner', 'Spring Balancer', 'RFID Antenna', 'Scanner', 'PPC', 'RFID Tag', 'IPC', 'Printer', 'Scanner', 'PPC', 'Scanner', 'RFID Antenna', 'Printer', 'IPC', 'RFID Antenna', 'Spring Balancer', 'Printer', 'IPC', 'Scanner', 'Scanner', 'Skid', 'PC', 'PLC', 'Printer', 'IPC', 'PPC', 'Spring Balancer', 'IPC', 'Skid', 'IPC', 'Network Cable', 'RFID Antenna', 'Scanner', 'Printer', 'Scanner', 'Printer', 'etc', 'etc', 'Spring Balancer', 'Scanner', 'Printer', 'PPC', 'Printer', 'Printer', 'PPC', 'PPC', 'Scanner', 'Scanner', 'PPC', 'RFID Antenna', 'RFID Antenna', 'RFID Antenna', 'Scanner', 'RFID Tag', 'Scanner', 'Spring Balancer', 'Skid', 'Scanner', 'Scanner', 'Scanner', 'Scanner', 'Skid', 'IPC', 'RFID Tag', 'Printer', 'Scanner', 'IPC', 'Printer', 'RFID Tag', 'RFID Antenna', 'Spring Balancer', 'Handle Keyboard', 'PPC', 'Scanner', 'Scanner', 'RFID Tag', 'Spring Balancer', 'Scanner', 'Scanner', 'PPC', 'PPC', 'Scanner', 'Scanner', 'PPC', 'IPC', 'Scanner', 'Spring Balancer', 'PPC', 'PPC', 'Scanner', 'Scanner', 'Scanner', 'Scanner', 'Printer', 'PPC', 'Network Cable', 'Scanner', 'IPC', 'Scanner', 'Scanner', 'PPC', 'Printer', 'Scanner', 'Scanner', 'IPC', 'Scanner', 'IPC', 'PPC', 'RFID Tag', 'Scanner', 'RFID Antenna', 'Scanner', 'PPC', 'Scanner', 'Scanner', 'PPC', 'RFID Antenna', 'IPC', 'Scanner', 'RFID Antenna', 'RFID Antenna', 'PPC', 'IPC', 'RFID Antenna', 'Printer', 'IPC', 'PPC', 'RFID Antenna', 'Scanner', 'Scanner', 'Spring Balancer', 'Spring Balancer', 'Scanner', 'Scanner', 'Engine', 'Scanner', 'Scanner', 'IPC', 'RFID Antenna', 'RFID Antenna', 'RFID Antenna', 'PPC', 'Printer', 'Scanner', 'RFID Tag', 'Printer', 'Scanner', 'Skid'],
        'Problem Reason': ['Program Error', 'Cable', 'Printhead', 'Key Ring', 'Damaged', 'Program Error', 'Network', 'Cable', 'Cable', 'Cable', 'SEQ Update', 'Cable', 'SEQ Update', 'Program Error', 'etc', 'Cable', 'Human Error', 'Malfunction', 'etc', 'etc', 'Malfunction', 'Damaged', 'Key Ring', 'Damaged', 'Malfunction', 'Key Ring', 'Malfunction', 'Human Error', 'Program Error', 'Malfunction', 'Key Ring', 'Power Cable', 'Cable', 'Malfunction', 'Network', 'Program Error', 'Malfunction', 'Damaged', 'Malfunction', 'Program Error', 'Malfunction', 'Damaged', 'etc', 'Program Error', 'etc', 'Malfunction', 'Program Error', 'Malfunction', 'Damaged', 'Malfunction', 'etc', 'Program Error', 'Human Error', 'Malfunction', 'Key Ring', 'Malfunction', 'Key Ring', 'Cartridge', 'Human Error', 'Human Error', 'Damaged', 'battery', 'Malfunction', 'Replacement', 'Malfunction', 'Paper', 'Replacement', 'Replacement', 'Malfunction', 'Damaged', 'Program Error', 'Malfunction', 'Malfunction', 'Malfunction', 'Malfunction', 'Human Error', 'Key Ring', 'Damaged', 'etc', 'Cable', 'Cable', 'Cable', 'Cable', 'etc', 'Program Error', 'etc', 'Network Cable', 'Cable', 'Program Error', 'Malfunction', 'SEQ Update', 'Malfunction', 'Damaged', 'Damaged', 'etc', 'battery', 'Key Ring', 'etc', 'Damaged', 'Cable', 'Cable', 'Replacement', 'SEQ Update', 'Malfunction', 'Cable', 'Malfunction', 'Program Error', 'Cable', 'Damaged', 'etc', 'Malfunction', 'Cable', 'Cable', 'Cable', 'Cable', 'Power Cable', 'Human Error', 'Human Error', 'Cable', 'Program Error', 'Malfunction', 'Cable', 'Malfunction', 'Malfunction', 'Cable', 'Cable', 'Program Error', 'Key Ring', 'Program Error', 'etc', 'SEQ Update', 'Key Ring', 'Malfunction', 'Damaged', 'Power Cable', 'Cable', 'Malfunction', 'Power Cable', 'Malfunction', 'Program Error', 'Malfunction', 'Malfunction', 'Malfunction', 'Power Cable', 'Program Error', 'Malfunction', 'Malfunction', 'Program Error', 'Program Error', 'Malfunction', 'Malfunction', 'Cable', 'Damaged', 'Damaged', 'Battery', 'Cable', 'SEQ Update', 'Key Ring', 'Human Error', 'Program Error', 'Malfunction', 'Malfunction', 'Malfunction', 'Malfunction', 'Malfunction', 'Cable', 'SEQ Update', 'Malfunction', 'Cable', 'SEQ Update'],
        'Category1': ['MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'Line', 'MES', 'Line', 'MES', 'MES', 'Line', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'Line', 'MES', 'MES', 'MES', 'Line', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'Line', 'MES', 'Line', 'MES', 'MES', 'Line', 'MES', 'MES', 'Line', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'Line', 'Line', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'Line', 'MES', 'MES', 'Line', 'MES', 'MES', 'MES', 'MES', 'Line', 'MES', 'Line', 'MES', 'MES', 'MES', 'MES', 'Line', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'Line', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'Line', 'Line', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'Line', 'MES', 'MES', 'MES', 'MES', 'MES', 'Line', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'Line', 'MES', 'Line', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'MES', 'Line', 'MES', 'MES', 'Line']

    }
)

LINES = {
    'ENG': ['IPC', 'Matching', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '11-1', '12', '13', '13-1', '13 Sub', '14', '15', '15-1', '17', '18', '19-1', '19', '20', '21', 'QC', 'Storage', 'Work Printer', 'WLBP', 'Printer(64)', 'Printer(206)', 'Printer(243)', 'Printer(236)', 'EMS', 'PDP', 'Starter', 'Comp', 'TranAssy', 'P2Board', 'TubeCheck', 'TMFeeding'],
    'FCM': ['IPC', 'Matching', 'AGV0', 'AGV1', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', 'QC', 'Shipping', 'Bridge', 'Member', 'WLBP', 'Printer(239)', 'Printer(242)', 'PDP', 'OS&D', 'P2Board', 'Axle LH', 'Axle RH', '', '', '', ''],
    'FCM Trolley': ['1', '2', 'Printer(65)', 'Printer(226)'],
    'RCM': ['IPC', 'Matching', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', 'QC', 'Shipping', 'Bridge', 'Member', 'Work Printer', 'Printer(55)', 'Printer(56)', 'Printer(63)', 'PDP', 'OS&D', 'P2Board', 'Spring', 'Axle LH', 'Axle RH', 'Shock', 'StabBar'],
    'CPM': ['IPC', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '21A', '22', '23', '24', '25', '25 Sub', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', 'QC', 'Shipping', 'Bridge', 'Work Printer', 'Printer(68)', 'Printer(59)', 'Printer(174)', 'KeySet', 'Wiring', 'OS&D', 'P2Board', 'Audio', 'TBar1', 'TBar4', 'TBar6', 'TBar7', 'TBarIPC', 'Trolley', 'PDP', 'CKD', 'HVAC', ''],
    'IP Sub': ['IPC', 'Matching', '3', '4', '7', '9', 'Feeding', 'PDP'],
    'CPM Trolley #1': ['0', '1', '2', 'Printer(66)', 'DPS controller', 'DPS module', 'DPS IPC'],
    'CPM Trolley #2': ['1', '2', '3', '4', '5', 'Printer(67)', 'DPS controller', 'DPS module', 'DPS IPC'],
    'FEM': ['IPC', 'Matching', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '12SCC', '13', '14', '15', '16', '17', 'QC', 'Shipping', 'Bridge', 'Work Printer', 'PDP', 'OS&D', 'SCC', 'P2Board', 'Trolley Unloading', 'BP Beam', 'Printer(251)', 'Hose Tube', 'Trolley Sub'],
    'FEM Trolley': ['2', '3', '5', 'Printer(70)', 'Printer(220)', 'Printer(231)', 'Printer(250)', 'Printer(243)', 'DPS controller', 'DPS module', 'PDP', 'DPS IPC', 'Sub PPC'],
    'BF': ['IPC', 'Matching', '3', '5', '6', '8', '9', '10', '12(QC)', 'Rework', 'Work Printer', 'OKI(51)', 'Shipping', 'Shipping Rack', 'DL3a(Sub)', 'Fog(Sub)', 'MQ4a(Sub)', 'NQ5a(Sub)', 'ON(Sub)', 'Grille Upr CKD(Sub)', 'UPRCVR(Sub)', 'Printer(61)', 'Printer(62)', 'Printer(63)', 'Printer(64)', 'Printer(65)', 'Printer(66)', 'Printer(67)', 'Printer(68)', 'OS&D', 'HAWA JIT', 'HAWA', 'CKD', 'DPS', 'DL3a(STD Press)', 'MQ4a(STD Press)', 'NQ5a(STD Press)', 'ON(STD Press)', 'ON GT Press(PE X-line)', 'MQ4a(Punch)', 'NQ5a(Punch)', 'ON(Punch)'],
    'BR': ['IPC', 'Matching', '2', '4', '5', '6', '8', '9', 'QC', 'Shipping', 'Bridge', 'Back Beam', 'Unloading', 'Work Printer', 'Printer(108)', 'Printer(240)', 'PDP', 'OS&D', 'P2Board', 'Vin Printer', 'ON PE Punch', 'DPS'],
    'CCR': ['21', '22', '23', '25'],
}
lines = list(LINES.keys())
#
# def update_radio(choice):
#     return gr.Radio.update(LINES[choice],  label="Stations", interactive=True)
def show_reports(search_val):
    temp = search_val.split('_', maxsplit=1)
    search_result= None
    if len(temp) == 1:
        search_result = sample_report[sample_report['Line'].str.contains(temp[0])]
    return search_result

with gr.Blocks() as block:
    with gr.Column():
        result = gr.Textbox(lines=10, Value='', interactive=True)
        for key, val in LINES.items():
            with gr.Column():
                globals()[f"{key}"] = gr.Button(value=f"{key}", elem_classes=str(key), elem_id=f"{key}")
                with gr.Row():
                    for i in val:
                        globals()[f"{key}_{i}"] = gr.Button(value=f"{key}_{i}", elem_classes=str(key), elem_id=f"{key}_{i}")
                        globals()[f"{key}_{i}"].style(full_width=False, size='sm')
                        globals()[f"{key}_{i}"].click(fn=show_reports(f"{key}_{i}"), inputs=result, outputs=result.value)

    block.launch()