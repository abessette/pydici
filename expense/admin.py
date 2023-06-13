# coding:utf-8
"""
Django administration setup
@author: Sébastien Renard <Sebastien.Renard@digitalfox.org>
@license: AGPL v3 or newer (http://www.gnu.org/licenses/agpl-3.0.html)
"""

from django.contrib import admin

from expense.models import Expense, ExpenseCategory, ExpensePayment


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("user", "description", "lead", "state", "chargeable", "creation_date", "update_date")
    ordering = ("-creation_date",)
    search_fields = ["description", "lead__name", "lead__client__organisation__company__name", "user__first_name", "user__last_name", "user__username"]
    list_filter = ["workflow_in_progress", "state", "chargeable", "corporate_card", "user"]
    actions = None


class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    actions = None


class ExpensePaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "payment_date", "user", "amount")


admin.site.register(Expense, ExpenseAdmin)
admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)
admin.site.register(ExpensePayment, ExpensePaymentAdmin)
