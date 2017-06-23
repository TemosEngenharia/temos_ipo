# -*- coding: utf-8 -*-
# ATT Generated at 2017-06-19 21:04:25

from odoo import models, fields, api

class IPOMain(models.Model):
    _name = 'ipo.main'
    _rec_name = 'task_key_id'
    _sql_constraints = [('ipo.main', 'unique (xml_source_filename)', 'XML já foi importado anteriormente!')]

    form_date_time = fields.Datetime(string=u'Data do Formulário')
    xml_source_filename = fields.Char(string=u'XML importado', default='')
    form_location_date = fields.Datetime(string=u'Data da Localização')
    checkin_call_datetime = fields.Datetime(string=u'Horário da ligação de Check-in')
    checkout_call_datetime = fields.Datetime(string=u'Horário da ligação de Check-out')
    entry_date_from_epoch = fields.Char(string=u'Data Epoch da Entrada')
    location_address = fields.Char(string=u'Endereço')
    location_x = fields.Char(string=u'longitude')
    location_y = fields.Char(string=u'latitude')
    location_date_from_epoch = fields.Char(string=u'Data Formulário from Epoch')
    form_name = fields.Char(string=u'Formulário')
    checkin_call_duration = fields.Integer(string=u'Duração da ligação Check-in?')
    checkin_attendant_by = fields.Char(string=u'Atendente que realizou o Check-in na PA')
    station_responsible_name = fields.Char(string=u'Nome do responsável pelo Posto')
    station_responsible_email = fields.Char(string=u'E-mail do posto')
    employee_firstname = fields.Char(string=u'Nome do Funcionário')
    employee_email = fields.Char(string=u'Email do Funcionário')
    employee_number = fields.Char(string=u'Nr. do Funcionário')
    employee_driver_id = fields.Integer(string=u'Código do Motorista')
    employee_group_name = fields.Char(string=u'Grupo do Funcionário')
    ot_task_number = fields.Char(string=u'Número da tarefa no OfficeTrack')
    task_description = fields.Char(string=u'Descrição do Chamado')
    task_notes = fields.Char(string=u'Notas da tarefa pelo atribuidor')
    task_data1 = fields.Char(string=u'Data1 - Resumo')
    task_data2 = fields.Char(string=u'Data2 - Prioridade')
    task_key_id = fields.Char(string=u'Data3 - TASK KEY ID para Link')
    task_type_code = fields.Char(string=u'Código do tipo da Tarefa do OfficeTrack')
    task_type_name = fields.Char(string=u'Nome do tipo da Tarefa do OfficeTrack')
    task_category_code = fields.Char(string=u'Código da Categoria da Tarefa do OfficeTrack')
    task_category_name = fields.Char(string=u'Nome da Categoria da Tarefa do OfficeTrack')
    task_customer_latitude = fields.Char(string=u'Latitude Cliente')
    task_customer_longitude = fields.Char(string=u'Longitude Cliente')
    task_customer_city = fields.Char(string=u'Cidade')
    task_customer_number = fields.Char(string=u'Código do Posto')
    task_customer_address_number = fields.Char(string=u'Nr')
    task_customer_name = fields.Char(string=u'Nome do Posto')
    task_customer_state = fields.Char(string=u'Estado')
    task_customer_street = fields.Char(string=u'Endereço')
    main_pic01_id = fields.Many2one('ipo.main_pic_files', u'PIC01|Foto do posto antes da instalação')
    main_pic02_id = fields.Many2one('ipo.main_pic_files', u'PIC02|Assinatura do Responsável do Posto')
    main_pic03_id = fields.Many2one('ipo.main_pic_files', u'PIC03|Colaborador 1 da Temos com os EPIs para atendimento')
    main_pic04_id = fields.Many2one('ipo.main_pic_files', u'PIC04|Colaborador 2 da Temos com os EPIs para atendimento')
    main_pic05_id = fields.Many2one('ipo.main_pic_files', u'PIC05|Foto EPC na pista')
    main_pic06_id = fields.Many2one('ipo.main_pic_files', u'PIC06|Foto do local ANTES de instalar o painel. (Foto na Vertical)')
    main_pic07_id = fields.Many2one('ipo.main_pic_files', u'PIC07|Foto do Painel Instalado Aberto. (Foto na Vertical)')
    main_pic08_id = fields.Many2one('ipo.main_pic_files', u'PIC08|Foto do Painel Instalado FECHADO. (Foto na Vertical)')
    main_pic09_id = fields.Many2one('ipo.main_pic_files', u'PIC09|Foto do Painel Instalado LACRADO com vista da CANALETA até o TETO. (Foto na Vertical)')
    main_pic10_id = fields.Many2one('ipo.main_pic_files', u'PIC10|Imagem da Câmera OCR (Foto na Vertical)')
    main_pic11_id = fields.Many2one('ipo.main_pic_files', u'PIC11|Imagem da Câmera Lateral (Foto na Vertical)')
    main_pic12_id = fields.Many2one('ipo.main_pic_files', u'PIC12|Foto do TETO ANTES (Foto na Vertical')
    main_pic13_id = fields.Many2one('ipo.main_pic_files', u'PIC13|Foto do TETO APÓS (Foto na Vertical)')
    main_pic14_id = fields.Many2one('ipo.main_pic_files', u'PIC14|Assinatura Colaborador Temos')
    main_pic15_id = fields.Many2one('ipo.main_pic_files', u'PIC15|Colaborador 1 da Temos com os EPIs para atendimento')
    main_pic16_id = fields.Many2one('ipo.main_pic_files', u'PIC16|Colaborador 2 da Temos com os EPIs para atendimento')
    main_pic17_id = fields.Many2one('ipo.main_pic_files', u'PIC17|Foto EPC na pista')
    main_pic18_id = fields.Many2one('ipo.main_pic_files', u'PIC18|Foto do local ANTES de instalar o painel. (Foto na Vertical)')
    main_pic19_id = fields.Many2one('ipo.main_pic_files', u'PIC19|Foto do Painel Instalado Aberto. (Foto na Vertical)')
    main_pic20_id = fields.Many2one('ipo.main_pic_files', u'PIC20|Foto do Painel Instalado FECHADO. (Foto na Vertical)')
    main_pic21_id = fields.Many2one('ipo.main_pic_files', u'PIC21|Foto do Painel Instalado LACRADO com vista da CANALETA até o TETO. (Foto na Vertical)')
    main_pic22_id = fields.Many2one('ipo.main_pic_files', u'PIC22|Imagem da Câmera OCR (Foto na Vertical)')
    main_pic23_id = fields.Many2one('ipo.main_pic_files', u'PIC23|Imagem da Câmera Lateral (Foto na Vertical)')
    main_pic24_id = fields.Many2one('ipo.main_pic_files', u'PIC24|Foto do TETO ANTES (Foto na Vertical)')
    main_pic25_id = fields.Many2one('ipo.main_pic_files', u'PIC25|Foto do TETO APÓS (Foto na Vertical)')
    main_pic26_id = fields.Many2one('ipo.main_pic_files', u'PIC26|ssinatura Colaborador Temos')
    main_pic27_id = fields.Many2one('ipo.main_pic_files', u'PIC27|Colaborador 1 da Temos com os EPIs para atendimento')
    main_pic28_id = fields.Many2one('ipo.main_pic_files', u'PIC28|Colaborador 2 da Temos com os EPIs para atendimento')
    main_pic29_id = fields.Many2one('ipo.main_pic_files', u'PIC29|Foto EPC na pista')
    main_pic30_id = fields.Many2one('ipo.main_pic_files', u'PIC30|Foto do local ANTES de instalar o painel. (Foto na Vertical)')
    main_pic31_id = fields.Many2one('ipo.main_pic_files', u'PIC31|Foto do Painel Instalado Aberto. (Foto na Vertical)')
    main_pic32_id = fields.Many2one('ipo.main_pic_files', u'PIC32|Foto do Painel Instalado FECHADO. (Foto na Vertical)')
    main_pic33_id = fields.Many2one('ipo.main_pic_files', u'PIC33|Foto do Painel Instalado LACRADO com vista da CANALETA até o TETO. (Foto na Vertical)')
    main_pic34_id = fields.Many2one('ipo.main_pic_files', u'PIC34|Imagem da Câmera OCR (Foto na Vertical)')
    main_pic35_id = fields.Many2one('ipo.main_pic_files', u'PIC35|Imagem da Câmera Lateral (Foto na Vertical)')
    main_pic36_id = fields.Many2one('ipo.main_pic_files', u'PIC36|Foto do TETO ANTES (Foto na Vertical)')
    main_pic37_id = fields.Many2one('ipo.main_pic_files', u'PIC37|Foto do TETO APÓS (Foto na Vertical)')
    main_pic38_id = fields.Many2one('ipo.main_pic_files', u'PIC38|Assinatura Colaborador Temos')
    main_pic39_id = fields.Many2one('ipo.main_pic_files', u'PIC39|Colaborador 1 da Temos com os EPIs para atendimento')
    main_pic40_id = fields.Many2one('ipo.main_pic_files', u'PIC40|Colaborador 2 da Temos com os EPIs para atendimento')
    main_pic41_id = fields.Many2one('ipo.main_pic_files', u'PIC41|Foto EPC na pista')
    main_pic42_id = fields.Many2one('ipo.main_pic_files', u'PIC42|Foto do local ANTES de instalar o painel. (Foto na Vertical)')
    main_pic43_id = fields.Many2one('ipo.main_pic_files', u'PIC43|Foto do Painel Instalado Aberto. (Foto na Vertical)')
    main_pic44_id = fields.Many2one('ipo.main_pic_files', u'PIC44|Foto do Painel Instalado FECHADO. (Foto na Vertical)')
    main_pic45_id = fields.Many2one('ipo.main_pic_files', u'PIC45|Foto do Painel Instalado LACRADO com vista da CANALETA até o TETO. (Foto na Vertical)')
    main_pic46_id = fields.Many2one('ipo.main_pic_files', u'PIC46|Imagem da Câmera OCR (Foto na Vertical)')
    main_pic47_id = fields.Many2one('ipo.main_pic_files', u'PIC47|Imagem da Câmera Lateral (Foto na Vertical)')
    main_pic48_id = fields.Many2one('ipo.main_pic_files', u'PIC48|Foto do TETO ANTES (Foto na Vertical)')
    main_pic49_id = fields.Many2one('ipo.main_pic_files', u'PIC49|Foto do TETO APÓS (Foto na Vertical)')
    main_pic50_id = fields.Many2one('ipo.main_pic_files', u'PIC50|Assinatura Colaborador Temos')
    main_pic51_id = fields.Many2one('ipo.main_pic_files', u'PIC51|Colaborador 1 da Temos com os EPIs para atendimento')
    main_pic52_id = fields.Many2one('ipo.main_pic_files', u'PIC52|Colaborador 2 da Temos com os EPIs para atendimento')
    main_pic53_id = fields.Many2one('ipo.main_pic_files', u'PIC53|Foto do local ANTES de instalar o servidor. (Foto na Vertical)')
    main_pic54_id = fields.Many2one('ipo.main_pic_files', u'PIC54|Foto da tela com a configuração do servidor. (Foto na Vertical)')
    main_pic55_id = fields.Many2one('ipo.main_pic_files', u'PIC55|Foto do Rack Instalado ABERTO. (Foto na Vertical)')
    main_pic56_id = fields.Many2one('ipo.main_pic_files', u'PIC56|Foto do Rack Instalado FECHADO. (Foto na Vertical)')
    main_pic57_id = fields.Many2one('ipo.main_pic_files', u'PIC57|Foto do Kit de Cartões de Cancelamento (Foto na Vertical)')
    main_pic58_id = fields.Many2one('ipo.main_pic_files', u'PIC58|Tela dos Cartões Cadastrados (Foto na Vertical)')
    main_pic59_id = fields.Many2one('ipo.main_pic_files', u'PIC59|Sentinela da Entrada (ANTES DA INSTALAÇÃO)')
    main_pic60_id = fields.Many2one('ipo.main_pic_files', u'PIC60|Sentinela da Entrada (APÓS A INSTALAÇÃO)')
    main_pic61_id = fields.Many2one('ipo.main_pic_files', u'PIC61|Assinatura do Responsável do Posto')
    main_pic62_id = fields.Many2one('ipo.main_pic_files', u'PIC62|Colaborador Temos com os EPIs (Selfie na Vertical)')
    main_pic63_id = fields.Many2one('ipo.main_pic_files', u'PIC63|Adesivo/Anexo a placa sentinela (Foto na Vertical)')
    main_pic64_id = fields.Many2one('ipo.main_pic_files', u'PIC64|Número da Bomba (Pump Number) (Foto na Vertical)')
    main_pic65_id = fields.Many2one('ipo.main_pic_files', u'PIC65|Moldura do Painel (Foto na Vertical)')
    main_pic66_id = fields.Many2one('ipo.main_pic_files', u'PIC66|Colaborador Temos com os EPIs (Selfie na Vertical)')
    main_pic67_id = fields.Many2one('ipo.main_pic_files', u'PIC67|Adesivo/Anexo a placa sentinela (Foto na Vertical)')
    main_pic68_id = fields.Many2one('ipo.main_pic_files', u'PIC68|Número da Bomba (Pump Number) (Foto na Vertical)')
    main_pic69_id = fields.Many2one('ipo.main_pic_files', u'PIC69|Moldura do Painel (Foto na Vertical)')
    main_pic70_id = fields.Many2one('ipo.main_pic_files', u'PIC70|Colaborador Temos com os EPIs (Selfie na Vertical)')
    main_pic71_id = fields.Many2one('ipo.main_pic_files', u'PIC71|Adesivo/Anexo a placa sentinela (Foto na Vertical)')
    main_pic72_id = fields.Many2one('ipo.main_pic_files', u'PIC72|Número da Bomba (Pump Number) (Foto na Vertical)')
    main_pic73_id = fields.Many2one('ipo.main_pic_files', u'PIC73|Moldura do Painel (Foto na Vertical)')
    main_pic74_id = fields.Many2one('ipo.main_pic_files', u'PIC74|Colaborador Temos com os EPIs (Selfie na Vertical)')
    main_pic75_id = fields.Many2one('ipo.main_pic_files', u'PIC75|Adesivo/Anexo a placa sentinela (Foto na Vertical)')
    main_pic76_id = fields.Many2one('ipo.main_pic_files', u'PIC76|Número da Bomba (Pump Number) (Foto na Vertical)')
    main_pic77_id = fields.Many2one('ipo.main_pic_files', u'PIC77|Moldura do Painel (Foto na Vertical)')
    main_pic78_id = fields.Many2one('ipo.main_pic_files', u'PIC78|Colaborador Temos com os EPIs (Selfie na Vertical)')
    main_pic79_id = fields.Many2one('ipo.main_pic_files', u'PIC79|Foto do Quadro Aberto ANTES de instalar o disjuntor. (Foto na Vertical)')
    main_pic80_id = fields.Many2one('ipo.main_pic_files', u'PIC80|Foto do Quadro Aberto APÓS de instalado o disjuntor com selo Sem Parar. (Foto na Vertical)')
    main_pic81_id = fields.Many2one('ipo.main_pic_files', u'PIC81|Infraestrutura Foto 1 (Foto na Vertical)')
    main_pic84_id = fields.Many2one('ipo.main_pic_files', u'PIC84|Infraestrutura Foto 4 (Foto na Vertical)')
    main_pic85_id = fields.Many2one('ipo.main_pic_files', u'PIC85|Foto dos funcionários do posto que receberam o treinamento.')
    main_pic86_id = fields.Many2one('ipo.main_pic_files', u'PIC86|Foto da Pista 1 liberada. (Foto na Vertical)')
    main_pic87_id = fields.Many2one('ipo.main_pic_files', u'PIC87|Foto da Pista 2 liberada. (Foto na Vertical)')
    main_pic88_id = fields.Many2one('ipo.main_pic_files', u'PIC88|Foto da Pista 3 liberada. (Foto na Vertical)')
    main_pic89_id = fields.Many2one('ipo.main_pic_files', u'PIC89|Foto da Pista 4 liberada. (Foto na Vertical)')
    main_pic90_id = fields.Many2one('ipo.main_pic_files', u'PIC90|Assinatura Colaborador Temos')
    main_pic90_id = fields.Many2one('ipo.main_pic_files', u'PIC90|Foto panorâmica da frente posto homologado (Foto na Horizontal)')
    main_pic91_id = fields.Many2one('ipo.main_pic_files', u'PIC91|Teste de Abastecimento Pista 1 (Foto na Vertical)')
    main_pic92_id = fields.Many2one('ipo.main_pic_files', u'PIC92|Teste de Abastecimento Pista 2 (Foto na Vertical)')
    main_pic93_id = fields.Many2one('ipo.main_pic_files', u'PIC93|Teste de Abastecimento Pista 3 (Foto na Vertical)')
    main_pic94_id = fields.Many2one('ipo.main_pic_files', u'PIC94|Teste de Abastecimento Pista 4 (Foto na Vertical)')
    main_pic95_id = fields.Many2one('ipo.main_pic_files', u'PIC95|Captura 1 da tela resultado do Homologa. (Foto na Vertical)')
    main_pic96_id = fields.Many2one('ipo.main_pic_files', u'PIC96|Captura 2 da tela resultado do Homologa. (Foto na Vertical)')
    main_pic97_id = fields.Many2one('ipo.main_pic_files', u'PIC97|Captura 3 da tela resultado do Homologa. (Foto na Vertical)')
    main_pic98_id = fields.Many2one('ipo.main_pic_files', u'PIC98|Captura 4 da tela resultado do Homologa. (Foto na Vertical)')
    main_pic99_id = fields.Many2one('ipo.main_pic_files', u'PIC99|Assinatura Colaborador que efetuou a homologação.')
    main_picasb01_id = fields.Many2one('ipo.main_pic_files', u'PICASB01|Captura da tela do Sistema Abastece Mostrando Bomba e Bico (Foto na Horizontal) (Pista 1 e 2)')
    main_picasb02_id = fields.Many2one('ipo.main_pic_files', u'PICASB02|Captura da tela do Sistema Abastece Mostrando Bomba e Bico (Foto na Horizontal) (Pista 3 e 4)')
    main_picasb03_id = fields.Many2one('ipo.main_pic_files', u'PICASB03|Foto Frontal Bomba Principal - Mostrar Número do Bico e Combustível')
    main_picasb04_id = fields.Many2one('ipo.main_pic_files', u'PICASB04|Foto do Pump Number Pista Principal')
    main_picasb05_id = fields.Many2one('ipo.main_pic_files', u'PICASB05|Foto Frontal Bomba Secundária - Mostrar Número do Bico e Combustível')
    main_picasb06_id = fields.Many2one('ipo.main_pic_files', u'PICASB06|Foto do Pump Number Pista Secundária')


class IPOMainPicFiles(models.Model):
    _name = 'ipo.main_pic_files'
    _rec_name = 'id'

    pic_file_guid = fields.Char(string=u'Guid da Foto')
    pic_filename = fields.Char(string=u'Nome do arquivo da Foto')
    pic_description = fields.Char(string=u'Descrição da Foto')
    pic_file_data = fields.Char(string=u'Foto')
    main_pic_ids = fields.One2many('ipo.main_pic_files', 'main_pic_id', u'Form File Id')
    main_pic_id = fields.Many2one('ipo.main', u'Fotos', ondelete='cascade', required=True)

