# =============================================================================
# Copyright 2020 NVIDIA. All Rights Reserved.
# Copyright 2019 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

from nemo.collections.nlp.data.datasets.sgd_dataset.sgd_dataset import SGDDataset
from nemo.collections.nlp.nm.data_layers.text_datalayer import TextDataLayer
from nemo.core.neural_types import ChannelType, LabelsType, LengthsType, NeuralType
from nemo.utils.decorators import add_port_docs

__all__ = ['SGDDataLayer']


class SGDDataLayer(TextDataLayer):
    """
    Data layer for Schema Guided Dialogue State Tracking Dataset.
    Args:
        dataset_split (str): train/ dev/ test,
        dialogues_processor (obj):  containt dialogue data,
        dataset_type (Dataset): Dataset Type,
        shuffle (bool): enables shuffling, default=False
        num_workers (int): number of workers
        batch_size (int): batch size
        pin_memory (bool): enables copying Tensors into CUDA pinned memory before returning them
    """

    @property
    @add_port_docs()
    def output_ports(self):
        """Returns definitions of module output ports.
        example_id_num (num): example ids
        service_id  (num): service ids
        is_real_example (bool): flag to determine is the example is valid
        utterance_ids (int): utterance ids
        utterance_segment (int): Denotes the identity of the sequence. Takes values 0 (system utterance) and 1 (user utterance)
        utterance_mask (int): Mask which takes the value 0 for padded tokens and 1 otherwise
        num_categorical_slots (int): Number of categorical slots present in the service
        categorical_slot_status (int): The status of each categorical slot in the service
        num_categorical_slot_values (int): Number of values taken by each categorical slot
        categorical_slot_values (int): The index of the correct value for each categorical slot
        num_noncategorical_slots (int): Number of non-categorical slots present in the service
        noncategorical_slot_status (int): The status of each non-categorical slot in the service
        noncategorical_slot_value_start (int): The index of the starting subword corresponding to the slot span for a non-categorical slot value
        noncategorical_slot_value_end (int): The index of the ending (inclusive) subword corresponding to the slot span for a non-categorical slot value
        start_char_idx (int): Start character indices in the original utterance corresponding to the tokens
        end_char_idx (int): Inclusive end character indices in the original utterance corresponding to the tokens
        num_slots (int): Total number of slots present in the service
        requested_slot_status (int): Takes value 1 if the corresponding slot is requested, 0 otherwise
        num_intents (int): Total number of intents present in the service
        intent_status_labels (int): Intent labels

        """
        return {
            "example_id_num": NeuralType(('B'), ChannelType()),
            "service_id": NeuralType(('B'), ChannelType()),
            "is_real_example": NeuralType(('B'), ChannelType()),
            "utterance_ids": NeuralType(('B', 'T'), ChannelType()),
            "utterance_segment": NeuralType(('B', 'T'), ChannelType()),
            "utterance_mask": NeuralType(('B', 'T'), ChannelType()),
            "num_categorical_slots": NeuralType(('B'), LengthsType()),
            "categorical_slot_status": NeuralType(('B', 'T'), LabelsType()),
            "num_categorical_slot_values": NeuralType(('B', 'T'), LengthsType()),
            "categorical_slot_values": NeuralType(('B', 'T'), LabelsType()),
            "num_noncategorical_slots": NeuralType(('B'), LengthsType()),
            "noncategorical_slot_status": NeuralType(('B', 'T'), LabelsType()),
            "noncategorical_slot_value_start": NeuralType(('B', 'T'), LabelsType()),
            "noncategorical_slot_value_end": NeuralType(('B', 'T'), LabelsType()),
            "start_char_idx": NeuralType(('B', 'T'), LabelsType()),
            "end_char_idx": NeuralType(('B', 'T'), LabelsType()),
            "num_slots": NeuralType(('B'), LengthsType()),
            "requested_slot_status": NeuralType(('B', 'T'), LabelsType()),
            "num_intents": NeuralType(('B'), LengthsType()),
            "intent_status_labels": NeuralType(('B'), LabelsType()),
        }

    def __init__(
        self,
        dataset_split,
        dialogues_processor,
        dataset_type=SGDDataset,
        shuffle=False,
        batch_size=1,
        num_workers=-1,
        pin_memory=False,
    ):

        dataset_params = {
            'dataset_split': dataset_split,
            'dialogues_processor': dialogues_processor,
        }
        super().__init__(
            dataset_type,
            dataset_params,
            batch_size=batch_size,
            shuffle=shuffle,
            num_workers=num_workers,
            pin_memory=pin_memory,
        )
