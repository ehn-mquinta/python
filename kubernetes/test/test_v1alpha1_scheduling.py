# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.16
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v1alpha1_scheduling import V1alpha1Scheduling  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1alpha1Scheduling(unittest.TestCase):
    """V1alpha1Scheduling unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1Scheduling
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1alpha1_scheduling.V1alpha1Scheduling()  # noqa: E501
        if include_optional :
            return V1alpha1Scheduling(
                node_selector = {
                    'key' : '0'
                    }, 
                tolerations = [
                    kubernetes.client.models.v1/toleration.v1.Toleration(
                        effect = '0', 
                        key = '0', 
                        operator = '0', 
                        toleration_seconds = 56, 
                        value = '0', )
                    ]
            )
        else :
            return V1alpha1Scheduling(
        )

    def testV1alpha1Scheduling(self):
        """Test V1alpha1Scheduling"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
