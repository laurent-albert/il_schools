# -*- coding: utf-8 -*-
# Copyright (c) 2017, IL and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import os
import babel.dates

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils.dateutils import parse_date
from frappe.utils import cint, cstr, flt, getdate, get_datetime, formatdate
from frappe.utils import get_site_name, get_site_path, get_site_base_path, get_path
#from DateTime import DateTime

import csv
#from frappe.utils.csvutils import read_csv_content

class ILStudentApplicantImport(Document):
	def import_sa_file(self):
		'''
			Trigger on import button
		'''

		columCSV = [['applicantid'],['salutation', 'e',['Monsieur','Mr'],['Madame','Mrs']],['last_name'],['usage_name'],
#					IdCandidat, Civilite, Nom, NomUsage
					['first_name'],['middle_name'],['social_security_number'],['ine_number'],
#					Prenom, Prenom2, NumSecu, NumIne
					['already_in_this_school'],[],
#					EtudiantLimayrac, Photo
					['date_of_birth','d','yyyy-mm-dd'],['place_of_birth'],
#					DateNaissance, LieuNaissance
					['nationality'],['address_line_1'],
#					Nationalite, Adresse
					['address_line_2'],['pincode'],
#					Adresse2, AdresseCp
					['city'],['country'],
#					AdresseVille, Pays
					[],['student_mobile_number'],
#					Tel, Tel2
					['student_email_id'],[],
#					Email, MotdePasse
#DateCreationCompte;Session; Formation;RefCandidature;DateCandidature;EtatInscription;Scolarite_Annees1;Scolarite_Niveau1;Scolarite_Etablissement1;Scolarite_Ville1;Scolarite_Annees2;Scolarite_Niveau2;Scolarite_Etablissement2;Scolarite_Ville2;Scolarite_Annees3;Scolarite_Niveau3;Scolarite_Etablissement3;Scolarite_Ville3;Diplome_Annee1;Diplome_Libelle1;Diplome_Filiere1;Diplome_Annee2;Diplome_Libelle2;Diplome_Filiere2;Diplome_Annee3;Diplome_Libelle3;Diplome_Filiere3;Langue1;Langue2;Langue3;Langue4;ConditionPaiement;Iban;Bic;Banque;AdresseBanque;CpBanque;VilleBanque;QualiteRespFinancier;Autre_Lien;Nom;Prenom;Adresse;Cp;Ville;Pays;Tel;Tel2;TelTravail;Email;SituationFamiliale;SituationPro;Profession;Entreprise;AdresseEntreprise;CpEntreprise;VilleEntreprise;Contact_Pere_Nom;Contact_Pere_Prenom;Contact_Pere_Adresse;Contact_Pere_Adresse;Contact_Pere_Cp;Contact_Pere_Ville;Contact_Pere_Pays;Contact_Pere_Tel;Contact_Pere_Tel2;Contact_Pere_TelTravail;Contact_Pere_Email;Contact_Pere_SituationFamiliale;Contact_Pere_SituationPro;Contact_Pere_Entreprise;Contact_Pere_AdresseEntreprise;Contact_Pere_CpEntreprise;Contact_Pere_VilleEntreprise;Contact_Mere_Nom;Contact_Mere_Prenom;Contact_Mere_Adresse;Contact_Mere_Adresse;Contact_Mere_Cp;Contact_Mere_Ville;Contact_Mere_Pays;Contact_Mere_Tel;Contact_Mere_Tel2;Contact_Mere_TelTravail;Contact_Mere_Email;Contact_Mere_SituationFamiliale;Contact_Mere_SituationPro;Contact_Mere_Entreprise;Contact_Mere_AdresseEntreprise;Contact_Mere_CpEntreprise;Contact_Mere_VilleEntreprise;
					[]]

					

		file_path = os.getcwd()+get_site_path()[1:].encode('utf8') + self.import_file

		with open(file_path, 'r') as csvfile:
			content = il_read_csv_content(csvfile.read())

#		wb = load_workbook(filename=file_path, read_only=True)
#		ws = wb.active

#		header = content[0][0].split(";")
		data = content[1:]
		for rowCSV in data:

			try:
				error = False
				rData = rowCSV[0].split(";")
#				program_doc = frappe.get_doc("Program", "BTSESF1)
				new_doc = frappe.new_doc("IL Student Applicant")
				new_doc.program = "BTS Économie Sociale Familiale"
				for j, value in enumerate(rData):
					if j < len(columCSV) and columCSV[j]:
#						new_doc.last_name = cell.value
						if len(columCSV[j]) <= 1:
							setattr(new_doc, columCSV[j][0], value)
						else:
							if columCSV[j][1] == "e":
								if columCSV[j][2][0] == value:
									setattr(new_doc, columCSV[j][0], columCSV[j][2][1])
								elif columCSV[j][3][0] == value:
									setattr(new_doc, columCSV[j][0], columCSV[j][3][1])
							elif columCSV[j][1] == "d":
#								setattr(new_doc, columName[j][0], formatdate(cell.value, columName[j][3]))
#								myDate = DateTime(value)
#								setattr(new_doc, columCSV[j][0], DateTime(value))
								myDate = getdate(value)
								setattr(new_doc, columCSV[j][0], getdate(value))
#								setattr(new_doc, columName[j][0], babel.dates.parse_date(cell.value, locale='fr_FR'))
#								parse_date('01.04.2004', locale='de_DE')
				new_doc.insert()
				new_doc.save()

			except Exception, e:
				error = True
				if new_doc:
					frappe.errprint(new_doc if isinstance(new_doc, dict) else new_doc.as_dict())
				frappe.errprint(frappe.get_traceback())

			finally:
				frappe.local.message_log = []

			if error:
				frappe.db.rollback()
			else:
				frappe.db.commit()

def il_read_csv_content(fcontent, ignore_encoding=False):
	rows = []

	if not isinstance(fcontent, unicode):
		decoded = False
		for encoding in ["utf-8", "windows-1252", "windows-1250"]:
			try:
				fcontent = unicode(fcontent, encoding)
				decoded = True
				break
			except UnicodeDecodeError:
				continue

		if not decoded:
			frappe.msgprint(_("Unknown file encoding. Tried utf-8, windows-1250, windows-1252."),
				raise_exception=True)

	fcontent = fcontent.encode("utf-8").splitlines(True)

	try:
		rows = []
		for row in csv.reader(fcontent):
			r = []
			for val in row:
				# decode everything
				val = unicode(val, "utf-8").strip()

				if val=="":
					# reason: in maraidb strict config, one cannot have blank strings for non string datatypes
					r.append(None)
				else:
					r.append(val)

			rows.append(r)

		return rows

	except Exception:
		frappe.msgprint(_("Not a valid Comma Separated Value (CSV File)"))
		raise