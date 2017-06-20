# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re


class OrderLineItemDiscount(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, type=None, percentage=None, amount_money=None, applied_money=None, scope=None):
        """
        OrderLineItemDiscount - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'percentage': 'str',
            'amount_money': 'Money',
            'applied_money': 'Money',
            'scope': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'percentage': 'percentage',
            'amount_money': 'amount_money',
            'applied_money': 'applied_money',
            'scope': 'scope'
        }

        self._name = name
        self._type = type
        self._percentage = percentage
        self._amount_money = amount_money
        self._applied_money = applied_money
        self._scope = scope

    @property
    def name(self):
        """
        Gets the name of this OrderLineItemDiscount.
        The discount's name.

        :return: The name of this OrderLineItemDiscount.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OrderLineItemDiscount.
        The discount's name.

        :param name: The name of this OrderLineItemDiscount.
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this OrderLineItemDiscount.
        The type of the discount. If it is created by API, it would be either FIXED_PERCENTAGE or FIXED_AMOUNT.  VARIABLE_* is not supported in API because the order is created at the time of sale and either percentage or amount has to be specified.

        :return: The type of this OrderLineItemDiscount.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this OrderLineItemDiscount.
        The type of the discount. If it is created by API, it would be either FIXED_PERCENTAGE or FIXED_AMOUNT.  VARIABLE_* is not supported in API because the order is created at the time of sale and either percentage or amount has to be specified.

        :param type: The type of this OrderLineItemDiscount.
        :type: str
        """

        self._type = type

    @property
    def percentage(self):
        """
        Gets the percentage of this OrderLineItemDiscount.
        The percentage of the tax, as a string representation of a decimal number.  A value of `7.25` corresponds to a percentage of 7.25%.

        :return: The percentage of this OrderLineItemDiscount.
        :rtype: str
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """
        Sets the percentage of this OrderLineItemDiscount.
        The percentage of the tax, as a string representation of a decimal number.  A value of `7.25` corresponds to a percentage of 7.25%.

        :param percentage: The percentage of this OrderLineItemDiscount.
        :type: str
        """

        self._percentage = percentage

    @property
    def amount_money(self):
        """
        Gets the amount_money of this OrderLineItemDiscount.
        The amount of the discount.

        :return: The amount_money of this OrderLineItemDiscount.
        :rtype: Money
        """
        return self._amount_money

    @amount_money.setter
    def amount_money(self, amount_money):
        """
        Sets the amount_money of this OrderLineItemDiscount.
        The amount of the discount.

        :param amount_money: The amount_money of this OrderLineItemDiscount.
        :type: Money
        """

        self._amount_money = amount_money

    @property
    def applied_money(self):
        """
        Gets the applied_money of this OrderLineItemDiscount.
        The amount of the money applied by the discount in an order.

        :return: The applied_money of this OrderLineItemDiscount.
        :rtype: Money
        """
        return self._applied_money

    @applied_money.setter
    def applied_money(self, applied_money):
        """
        Sets the applied_money of this OrderLineItemDiscount.
        The amount of the money applied by the discount in an order.

        :param applied_money: The applied_money of this OrderLineItemDiscount.
        :type: Money
        """

        self._applied_money = applied_money

    @property
    def scope(self):
        """
        Gets the scope of this OrderLineItemDiscount.
        The scope of the discount.

        :return: The scope of this OrderLineItemDiscount.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this OrderLineItemDiscount.
        The scope of the discount.

        :param scope: The scope of this OrderLineItemDiscount.
        :type: str
        """

        self._scope = scope

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
