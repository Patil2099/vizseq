# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#

from typing import List, Optional, Dict

from nltk.translate.ribes_score import sentence_ribes

from vizseq.scorers import register_scorer, VizSeqScorer, VizSeqScore


def _get_sent_ribes(
        hypothesis: List[str], references: List[List[str]],
        extra_args: Optional[Dict[str, str]] = None,
) -> List[float]:
    joined_references = list(zip(*references))
    return [sentence_ribes(r, h) for r, h in zip(joined_references, hypothesis)]


@register_scorer('ribes', 'RIBES')
class RIBESScorer(VizSeqScorer):
    def score(
            self, hypothesis: List[str], references: List[List[str]],
            tags: Optional[List[List[str]]] = None
    ) -> VizSeqScore:
        return self._score_multiprocess_averaged(
            hypothesis, references, tags, sent_score_func=_get_sent_ribes
        )
