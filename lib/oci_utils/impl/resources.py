#
# Copyright (c) 2018, 2019 Oracle and/or its affiliates. All rights reserved.
# Licensed under the Universal Permissive License v 1.0 as shown
# at http://oss.oracle.com/licenses/upl.


import six


class OCIAPIAbstractResource(object):
    """ Ancestor class for most OCI objects
    """
    _ignore_dict_items = ["swagger_types", "attribute_map"]
    _complex_items = ["launch_options", "source_details"]

    def __init__(self, data, session):
        """
        Initialisation of the OCIAPIAbstractResource object.

        Parameters
        ----------
        data: dict
            resource data
        session: OCISession
            OCI SDK session

        Returns
        -------
            No return value.
        """
        assert session.__class__.__name__ == 'OCISession', \
            'Invalid type for session'
        self._data = data
        self._oci_session = session
        self._ocid = self._data.id

    def __dict__(self):
        """
        Override __dict__ attribute.

        Returns
        -------
            dict
                The new dictionary.
        """
        return self._get_dict_recursive()

    def get_ocid(self):
        """
        Get the OCID.

        Returns
        -------
            str
                The OCID.
        """
        return self._ocid

    def _get_dict_recursive(self):
        """
        Get dict for and object which has embedded complex object.

        Returns
        -------
            dict
                The recursive object dictionary.
        """
        try:
            data_dict = {}
            for key in vars(self._data):
                value = getattr(self._data, key)
                if key.startswith('_'):
                    key = key[1:]
                # Handle complex types
                if key in OCIAPIAbstractResource._ignore_dict_items:
                    continue
                if type(value) in [int, bool]:
                    data_dict[key] = value
                elif isinstance(value, six.string_types):
                    data_dict[key] = value.strip()
                elif value is None:
                    data_dict[key] = ''
                elif key in OCIAPIAbstractResource._complex_items:
                    data_dict[key] = OCIAPIAbstractResource._get_dict_recursive(
                        value)
                else:
                    data_dict[key] = value
            return data_dict
        except Exception:
            return None

    def get_display_name(self):
        """
        Get the display name.

        Returns
        -------
            str
                The display name.
        """
        return self._data.display_name

    def get_availability_domain(self):
        """
        Get the availability domain.

        Returns
        -------
            str
                The domain name.
        """
        return self._data.availability_domain

    def get_compartment(self):
        """
        Get the compartment id.

        Returns
        -------
            str
                The compartment id.
        """
        return self._oci_session.get_compartment(self._data.compartment_id)

    def __str__(self):
        """
        Override the string representation of the instance.

        Returns
        -------
            str
                The string representation of the instance.
        """
        return "'%s' (%s)" % (self.get_display_name(), self.get_ocid())

    def __eq__(self, other):
        """
        Override the __eq__ behaviour.

        Parameters
        ----------
        other: OCIAPIAbstractResource
            The instance to test.

        Returns
        -------
            bool
                True or False.
        """
        if not isinstance(other, OCIAPIAbstractResource):
            return False
        return self._ocid == other._ocid

    def __ne__(self, other):
        """
        Override the __ne__ behaviour.

        Parameters
        ----------
        other: OCIAPIAbstractResource
            The instance to test.

        Returns
        -------
            bool
                True or False.
        """
        return not self._ocid == other._ocid

    def __gt__(self, other):
        """
        Override the __gt__ behaviour.

        Parameters
        ----------
        other: OCIAPIAbstractResource

        Returns
        -------
            bool
                True or False.
        """
        assert isinstance(other, OCIAPIAbstractResource), \
            'wrong type in comparison'
        # at abstract level not much sense sorting: sort OCIDs then
        return self._ocid > other._ocid

    def __lt__(self, other):
        """
        Override the __lt__ behaviour.

        Parameters
        ----------
        other: OCIAPIAbstractResource
            The instance to test.

        Returns
        -------
            bool
                True or False.
        """
        assert isinstance(other, OCIAPIAbstractResource), \
            'wrong type in comparison'
        # at abstract level not much sense sorting: sort OCIDs then
        return self._ocid < other._ocid